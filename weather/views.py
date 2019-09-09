from django.shortcuts import render
import requests
from weatherApp.api_call import get_weather_data
from weather import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherAppView(APIView):
    """Describes how to Interact with the weather App"""

    serializer_class = serializers.WeatherSerializer

    def get(self, request, format=None):
        """Returns A set of instructions for this app"""
        instructions = [
            'Enter your city and get an updated weather forcust'
        ]
        return Response({"instructions": instructions})

    def post(self, request, format=None):
        """Responsible for getting the weather"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            # make a request to the weatherAPI
            weather_data = get_weather_data(city)

        return Response(weather_data)


