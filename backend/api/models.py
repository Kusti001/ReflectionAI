from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ai_summary = models.TextField(null=True, blank=True) 
    sentiment_score = models.FloatField(null=True, blank=True)  # -1..1
    emotions = models.JSONField(default=dict)  # {'joy': 0.8, 'sadness': 0.2}
    ai_processed = models.BooleanField(default=False)
    ai_processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date.strftime('%Y-%m-%d')}"
    
    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ['-date']  # order by date descending
        unique_together = ['user', 'date']  # one entry per day for one user

