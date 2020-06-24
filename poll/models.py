from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=48)

    def __str__(self):
        return "{}-Token".format(self.user)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        # return self.text
        return "{}-{}".format(self.date, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return self.text
        return "{}-{}".format(self.date, self.amount)


