from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    _parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)


class Profile(models.Model):
    STATUS_CHOICES = (
        (0, 'disabled'),
        (1, 'active'),
        (3, 'inactive'),
    )
    nick_name = models.CharField(max_length=255, default='')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, db_index=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='_profile', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nick_name