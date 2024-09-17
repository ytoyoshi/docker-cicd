from django.db import models

class Page(models.Model):
    icon = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255, default="home")
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.title