from django.db import models
from django.utils import timezone
from django.urls import reverse

class Notification(models.Model):
    TYPE_CHOICES = [
        ('Payment', 'Payment'),
        ('Subscription', 'Subscription'),
        ('Discount', 'Discount'),
    ]

    title = models.CharField(max_length=255, default='NULL')
    recipient = models.EmailField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='NULL')
    details = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': str(self.pk)})

class Alert(models.Model):
    CATEGORY_CHOICES = [
        ('Subscription', 'Subscription'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField()
    read = models.BooleanField(default=False)
