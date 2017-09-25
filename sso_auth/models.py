'''from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        # Ensure that a username is set
        if not username:
            raise ValueError('Users must have a valid username')

        account = self.model(
            username=kwargs.get('username')
        )
        password = "#####################"
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None, **kwargs):
        account = self.create_user(email, password, kwargs)
        account.save()
        return account
        '''
