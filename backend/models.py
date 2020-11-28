from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=200)
    status = models.BooleanField('Status')

    def __str__(self):
        return self.text
