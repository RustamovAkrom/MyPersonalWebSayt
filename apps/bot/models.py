from django.conf import settings
from django.db import models
from apps.shared.models import TimestempedModel


class BotUserMessage(TimestempedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bot_user_messages",
    )
    message_text = models.TextField()
    message_type = models.CharField(max_length=50, choices=[
        ('suggestion', 'Taklif'),
        ('complaint', 'Shikoyat'),
        ('feedback0', 'Fikr-mulohaza'),
        ('other', 'Boshqa'),
    ])
    
    def __str__(self) -> str:
        return f"{self.user} - {self.message_type}"
