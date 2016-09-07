from django.db import models
from django.utils.timezone import now

class Project(models.Model):
  project_title = models.CharField(max_length=250)
  created_date = models.DateTimeField(default=now, blank=True)

  def __str__(self):
    return self.project_title

class Note(models.Model):
  note_title = models.CharField(max_length=250)
  body = models.CharField(max_length=10000)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=now, blank=True)

  def __str__(self):
    return self.note_title

# convert code to SQL file, make change to database:
# python manage.py makemigrations notes
# run it:
# python manage.py migrate