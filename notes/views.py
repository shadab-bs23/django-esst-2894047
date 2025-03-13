from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = "notes/notes_detail.html"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = 'popular_notes'
    template_name = "notes/popular_notes_list.html"
    
    def get_queryset(self):
        return Notes.objects.filter(likes__gt = 5)

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist!")
        
#     return render(request, "notes/notes_detail.html", {'note': note})