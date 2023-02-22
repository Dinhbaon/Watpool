from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator

class AccountManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)
    def create_user(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email)
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password): 
        user = self.create_user(email=self.normalize_email(email),
                                password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    def delete_superuser(self, email):
        self.delete()


class Account(AbstractBaseUser): 
    email = models.EmailField(max_length=60, unique=True, verbose_name="email", 
            validators=[EmailValidator(message='Use @uwaterloo.ca email',allowlist=['uwaterloo.ca'])])
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


    objects = AccountManager()
    USERNAME_FIELD = 'email'
# Create your models here.
