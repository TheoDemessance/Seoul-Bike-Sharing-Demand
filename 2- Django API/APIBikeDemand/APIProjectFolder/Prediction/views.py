from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .apps import PredictionConfig
import pandas as pd
import numpy as np

# Create your views here.
@api_view(['GET', 'POST'])

def api_add(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        # Do nothing
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
    return Response(response_dict, status=status.HTTP_201_CREATED)

# Class based view to add numbers
class Add_Values(APIView):
    def post(self, request, format=None):
        sum = 0
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
        return Response(response_dict, status=status.HTTP_201_CREATED)

# Class based view to predict based on IRIS model
class Bike_Model_Predict(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_regressor = PredictionConfig.regressor
        y_pred = loaded_regressor.predict(X)
        y_pred = pd.Series(np.expm1(y_pred))
        response_dict = {"Predicted Bike Demand": y_pred[0]}
        return Response(response_dict, status=200)