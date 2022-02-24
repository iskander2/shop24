from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


from .utils import get_random_string

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=500)
    verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



# Create your models here.
class ConfirmationCode(models.Model):
    code = models.CharField(max_length=10,verbose_name='КОД')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name ="Код"
        verbose_name_plural= "Коды"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string()
        super(ConfirmationCode, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

