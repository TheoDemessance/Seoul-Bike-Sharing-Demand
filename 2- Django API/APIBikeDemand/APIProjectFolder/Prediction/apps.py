from django.apps import AppConfig
import pandas as pd
from joblib import load
import os

class PredictionConfig(AppConfig):
    name = 'Prediction'
    #REGRESSOR_FOLDER = Path("regressor")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REGRESSOR_FOLDER = os.path.join(BASE_DIR, 'Prediction/regressor/')
    #REGRESSOR_FILE = REGRESSOR_FOLDER / "BikeDemandRandomForestRegressor.joblib"
    REGRESSOR_FILE = os.path.join(REGRESSOR_FOLDER, "BikeDemandRandomForestRegressor.joblib")
    regressor = load(REGRESSOR_FILE)