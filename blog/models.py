from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    creates a Post table in sqlite3 database
    automatically generates sql queries - can be seen by python manage.py sqlmigrate blog 0001

    :params models.Model: what the class inherits from
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE deletes all posts of the user if user deleted, one way only

    def __str__(self):
        """
        returns the class objects as a string

        :return: str 
        """
        return self.title

    def get_absolute_url(self):
        """
        to let Django know how to find the location of the specific blog post

        :return: the reverse function will return the full url as a string so that the view can handle the redirect
        """
        return reverse('post-detail', kwargs={'pk': self.pk})