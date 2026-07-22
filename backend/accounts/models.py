from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model. Starting with this now avoids painful migrations later
    if we need extra fields (avatar, bio, etc.) as the project grows.
    """
    email = models.EmailField(unique=True)
    avatar_color = models.CharField(
        max_length=7,
        default='#4F46E5',
        help_text='Hex color used for this user\'s cursor/avatar in collaborative editing'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
