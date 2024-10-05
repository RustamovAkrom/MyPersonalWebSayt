from django.db import models


class TimestempedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugstempedModel(models.Model):
    slug = models.CharField(max_length=200)

    class Meta:
        abstract = True
        