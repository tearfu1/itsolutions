from django.db import models

# Create your models here.
class Prompts(models.Model):
    prompt = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
