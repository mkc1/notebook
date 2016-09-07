from django.db import models
from django.utils.timezone import now

class Note(models.Model):
  note_title = models.CharField(max_length=250)
  body = models.CharField(max_length=10000)
  created_date = models.DateTimeField(default=now, blank=True)

  #redirect to details of note
  def get_absolute_url(self):
    return reverse('notes:detail', kwargs={'pk' : self.pk})

  #display name
  def __str__(self):
    return self.note_title