from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def __str__(self):
  return f'{self.name} ({self.id})'

  def get_absolute_url(self):
   return reverse('detail', kwargs={'finch_id': self.id})
