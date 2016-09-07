from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note

class IndexView(generic.ListView):
  template_name = 'notes/index.html'
  def get_queryset(self):
    return Note.objects.all()

class DetailView(generic.DetailView):
  model = Note
  template_name = 'notes/detail.html'

class NoteCreate(CreateView):
  model = Note
  fields = ['note_title', 'body']