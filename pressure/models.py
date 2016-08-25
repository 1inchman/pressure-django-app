from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Measurment(models.Model):
    systolic = models.FloatField()
    diastolic = models.FloatField()
    date = models.DateTimeField()
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.systolic
