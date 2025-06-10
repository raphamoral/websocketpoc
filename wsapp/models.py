from django.db import models


class DataHistory(models.Model):
    api_type = models.IntegerField()
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"api:{self.api_type} at {self.timestamp}"
