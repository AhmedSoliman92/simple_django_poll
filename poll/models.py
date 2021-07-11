from os import truncate
from django.db import models
from datetime import timedelta
# Create your models here.


class Polls(models.Model):
    poll_title = models.CharField(max_length=50)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, null=True)
    option4 = models.CharField(max_length=100, null=True)
    option5 = models.CharField(max_length=100, null=True)
    c_option1 = models.IntegerField(default=0)
    c_option2 = models.IntegerField(default=0)
    c_option3 = models.IntegerField(default=0)
    c_option4 = models.IntegerField(default=0)
    c_option5 = models.IntegerField(default=0)

    is_valid = models.DurationField(default=timedelta(days=7))

    def __str__(self):
        return self.poll_title
