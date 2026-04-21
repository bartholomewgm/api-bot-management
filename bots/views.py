from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Bot
from .serializers import BotSerializer


class BotViewSet(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
