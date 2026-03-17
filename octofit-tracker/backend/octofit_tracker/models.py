from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True
    )

class Activity(models.Model):
    username = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.username} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for_team_name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    username = models.CharField(max_length=150)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.username} - {self.points}"
