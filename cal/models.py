from django.db import models

class DayEntry(models.Model):
    date = models.DateField(unique=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

