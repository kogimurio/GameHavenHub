from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OngoingGame, LoginLog  # Import the required models

@receiver(post_save, sender=OngoingGame)
def log_ongoing_game(sender, instance, created, **kwargs):
    if created:  # If a new OngoingGame instance is created
        LoginLog.objects.create(user=instance.user)  # Adjust according to your actual logging needs
