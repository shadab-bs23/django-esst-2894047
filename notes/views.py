from django.shortcuts import render, get_object_or_404
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404

def change_visibility(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

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