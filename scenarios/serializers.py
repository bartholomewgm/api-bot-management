from rest_framework import serializers
from .models import Scenario, ScenarioStep


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"


class ScenarioStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioStep
        fields = "__all__"
