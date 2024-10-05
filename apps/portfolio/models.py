from django.conf import settings
from django.db import models
from apps.shared.models import TimestempedModel, SlugstempedModel


class Project(TimestempedModel, SlugstempedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        return self.title
    