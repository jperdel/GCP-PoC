import optuna
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier



def objective(trial: optuna.trial, X: pd.DataFrame, y: pd.Series, random_seed:int, kfolds:int):
    '''
    Objective function to optimice with Optuna

    Params:
        trial: Optuna trial
        X: features
        y: target
        random_seed: random seed for the K-Folds and the Random Forest
        kfolds: number of folds in the K-Folds

    Returns:
        Mean AUC score of the trial
    '''

    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 10),
        "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 5),
        "max_features": trial.suggest_categorical(
            "max_features", ["sqrt", "log2"]
        ),
        "random_state": random_seed,
        "n_jobs": -1,
    }

    kf = KFold(
        n_splits=kfolds,
        shuffle=True,
        random_state=random_seed
    )

    fold_scores = []

    with mlflow.start_run(nested=True):
        mlflow.log_params(params)

        for fold, (train_idx, val_idx) in enumerate(kf.split(X)):
            X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
            y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

            model = RandomForestClassifier(**params)
            model.fit(X_train, y_train)

            y_pred = model.predict_proba(X_val)[:, 1]
            score = roc_auc_score(y_val, y_pred)

            fold_scores.append(score)

            mlflow.log_metric(f"roc_auc_fold_{fold}", score)

        mean_score = np.mean(fold_scores)
        std_score = np.std(fold_scores)

        mlflow.log_metric("roc_auc_mean", mean_score)
        mlflow.log_metric("roc_auc_std", std_score)

    return mean_score


def run_mlflow_cv(X: pd.DataFrame, y: pd.Series, experiment_name: str, random_seed:int=None, kfolds:int=5, n_trials:int=10):
    '''
    Run the hyperparameter optimization and register the values with MLFlow.

    Params:
        X: features
        y: target
        random_seed: random seed for the Optuna study, the K-Folds and the Random Forest
        kfolds: number of folds in the K-Folds
        n_trials: number of Optuna trials
    '''


    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name="optuna_rf_cv"):

        study = optuna.create_study(
            direction="maximize",
            sampler=optuna.samplers.TPESampler(seed=random_seed)
        )

        study.optimize(
            lambda trial: objective(trial, X, y, random_seed, kfolds),
            n_trials=n_trials
        )

        mlflow.log_params(study.best_params)
        mlflow.log_metric("best_cv_score", study.best_value)