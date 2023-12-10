from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        Group, Permission, PermissionsMixin)
from django.db import models


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, username, password=None):
        if not email:
            raise ValueError("Direccion de correo electronico obligatoria")
        
        if not username:
            raise ValueError("Nombre de usuario obligatorio")

        user = self.model(
            email = self.normalize_email(email), 
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email), 
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):

    email      = models.EmailField(max_length=150, unique=True)
    username   = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name  = models.CharField(max_length=150, blank=True)
    phone_number   = models.CharField(max_length=15, blank=True)
    # User Status
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created      = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomAccountManager()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='account_groups',  
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='account_user_permissions',  
    )

class UserProfile(models.Model):
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1  = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city            = models.CharField(blank=True, max_length=20)
    comuna          = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1}'