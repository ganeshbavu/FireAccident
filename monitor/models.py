from django.db import models

class FireAlert(models.Model):
    temperature = models.FloatField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperature} - {self.status}"