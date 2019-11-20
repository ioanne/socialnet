from django.db import models
from django.utils import timezone

from apps.auth.models import Profile


class Site(models.Model):
    
    """Site Model"""

    STATUS_CHOICES = (
        (0, 'disabled'),
        (1, 'active'),
        (2, 'inactive'),
        (3, 'maintenance'),
    )
    profile = models.ForeignKey(
        Profile,
        related_name='sites',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created = models.DateTimeField(default=timezone.now)
    domain = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, db_index=True)

    def __str__(self):
        return '%s' % self.domain


class Page(models.Model):

    """Page Model"""

    title = models.CharField(max_length=255)
    site = models.ForeignKey(
        'Site',
        related_name='pages',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return '%s' % self.title


class Section(models.Model):

    """Section Model"""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    page = models.ForeignKey(
        'Page',
        related_name='sections',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return '%s' % self.title


class Image(models.Model):
    
    """Image Model"""

    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    section = models.ForeignKey(
        'Section',
        related_name='images',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return '%s' % self.title