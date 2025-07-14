from django.db import models


class DiscordMessage(models.Model):
    content = models.TextField(null=True, blank=True)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"DiscordMessage #: {self.id} (Sent: {self.sent})"
