from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='General')
    priority = models.IntegerField(default=1)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title