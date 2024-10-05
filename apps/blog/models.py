from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from apps.shared.models import TimestempedModel, SlugstempedModel


class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    

class Post(TimestempedModel, SlugstempedModel):
    class Status(models.TextChoices):
        DRAFT = 'df', 'Draft'
        PUBLISHED = 'pd', 'Published'
    
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    content = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish', )
        indexes = (
            models.Index(fields=['-publish']),
        )

    def __str__(self) -> str:
        return self.title
    

class Comment(TimestempedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )


class Contact(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contacts",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}, {self.subject}"