from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Notes, Video

# Create your views here.
def introduction(request):
    """renders the intro to mtb"""
    return render(request, 'mtb/introduction.html')

class NotesListView(CreateView, ListView):
    """Add and view Notes"""
    model = Notes
    template_name = 'mtb/notes.html'
    context_object_name = 'notes_list'
    fields = ['title', 'description', 'link']
    success_url = reverse_lazy('mtb-notes')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NotesUpdateView(UpdateView):
    """Edit Notes"""
    model = Notes
    template_name = 'mtb/notes.html'
    context_object_name = 'notes_list'
    fields = ['title', 'description', 'link']
    success_url = reverse_lazy('mtb-notes')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def notes_delete_view(request, id):
    context ={}
    obj = get_object_or_404(Notes, id = id)

    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # notes-list-view
        return HttpResponseRedirect(reverse_lazy('mtb-notes'))
    

class VideosListView(ListView):
    """General questions"""
    model = Video
    template_name = 'mtb/videos.html'
    context_object_name = 'videos_list'
