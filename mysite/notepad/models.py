from django.db import models
from django.urls import reverse
# Create your models here.
class Note(models.Model):
    image   = models.ImageField(upload_to='images/', null=True)
    title   = models.TextField()
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={"id": self.id})

