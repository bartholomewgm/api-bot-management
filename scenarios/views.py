from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Scenario, ScenarioStep
from .serializers import ScenarioSerializer, ScenarioStepSerializer


class ScenarioViewSet(ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ScenarioStepViewSet(ModelViewSet):
    queryset = ScenarioStep.objects.all()
    serializer_class = ScenarioStepSerializer
