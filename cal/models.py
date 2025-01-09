from django.db import models

class DayEntry(models.Model):
    date = models.DateField(unique=True)
    content_left = models.TextField(blank=True)  # Contenuto del primo riquadro
    content_right = models.TextField(blank=True)  # Contenuto del secondo riquadro

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

