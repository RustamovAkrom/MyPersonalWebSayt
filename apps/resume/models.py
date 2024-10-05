from django.conf import settings
from django.db import models
from apps.shared.models import TimestempedModel


class Resume(TimestempedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_resume",
    )
    file = models.FileField(upload_to="resumes/")

    def __str__(self) -> str:
        return f"Resume: {self.user.username}"
    