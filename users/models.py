from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    creates a Profile model for a user's profile picture

    :params models.Model: what the class inherits from
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE deletes the profile is user is deleted, only one way
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        returns the class objects as a string

        :return: str 
        """
        return f"{self.user.username} Profile"