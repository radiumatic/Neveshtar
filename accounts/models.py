from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    @property
    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)
