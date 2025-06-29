from django.contrib.auth.models import User
from django.db import models
import json


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField(default=dict, blank=True)

    def get_preference(self, key, default=None):
        return self.preferences.get(key, default)

    def set_preference(self, key, value):
        self.preferences[key] = value
        self.save()

    def update_preferences(self, prefs_dict):
        self.preferences.update(prefs_dict)
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Profile"