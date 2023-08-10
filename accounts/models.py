from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(null=False, blank=False, upload_to='user_pics', verbose_name='Фото профиля')
    review_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )