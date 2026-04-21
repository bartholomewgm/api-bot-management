from django.db import models


class Scenario(models.Model):
    bot = models.ForeignKey(
        'bots.Bot', on_delete=models.CASCADE, related_name="scenarios")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


class ScenarioStep(models.Model):
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE, related_name="steps")
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    prompt = models.TextField()
    next_step = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL)
