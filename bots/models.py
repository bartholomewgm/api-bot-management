from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    system_prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
