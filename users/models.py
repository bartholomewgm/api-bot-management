from django.db import models


class UserSession(models.Model):
    user_id = models.CharField(max_length=255)
    bot = models.ForeignKey('bots.Bot', on_delete=models.CASCADE)
    current_step = models.ForeignKey(
        'scenarios.ScenarioStep', null=True, on_delete=models.SET_NULL)
    context = models.JSONField(default=dict)
