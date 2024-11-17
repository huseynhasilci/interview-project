"""Database models."""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, # functinonality for the basic authentication system.
    BaseUserManager,
    PermissionsMixin
)

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    responsible_part_type = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user."""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creating super user method. Which is read by the django cli"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="user", null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Part(models.Model):
    part_type = models.CharField(max_length=50)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="parts", null=True)
    stock_count = models.IntegerField(default=0)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part_type} for {self.aircraft.aircraft_name}"


class Aircraft(models.Model):
    aircraft_name = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)
    part_ids = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="aircraft", null=True)

    def __str__(self):
        return self.aircraft_name
