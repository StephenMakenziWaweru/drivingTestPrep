from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView
from .models import Notes, Video
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def introduction(request):
    """renders the intro to mtb"""
    return render(request, 'mtb/introduction.html')

class NotesListView(SuccessMessageMixin, CreateView, ListView):
    """Add and view Notes"""
    model = Notes
    template_name = 'mtb/notes.html'
    context_object_name = 'notes_list'
    fields = ['title', 'description', 'link']
    success_url = reverse_lazy('mtb-notes')
    success_message = "Resource was added successfully"
    order_by = '-id'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NotesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    """Edit Notes"""
    model = Notes
    template_name = 'mtb/notes_edit.html'
    fields = ['title', 'description', 'link']
    success_url = reverse_lazy('mtb-notes')
    success_message = "Resource was updated successfully"
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False

@login_required
def notes_delete_view(request, id):
    context ={}
    obj = get_object_or_404(Notes, id = id)

    if request.method =="POST":
        if request.user == obj.owner:
            # delete object
            obj.delete()
            # after deleting redirect to
            # notes-list-view
            messages.success(request, f'Resource deleted successfully!!')
            return HttpResponseRedirect(reverse_lazy('mtb-notes'))
        else:
            messages.error(request, f'Cannot delete a resource you don\'t own!!')
            return HttpResponseRedirect(reverse_lazy('mtb-notes'))
    
    return render(reverse_lazy('mtb-notes'))
    

class VideosListView(LoginRequiredMixin, SuccessMessageMixin, CreateView, ListView):
    """MTB videos"""
    model = Video
    template_name = 'mtb/videos.html'
    context_object_name = 'videos_list'
    fields = ['title', 'description', 'link']
    success_url = reverse_lazy('mtb-videos')
    success_message = "Video was added successfully"
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        
        return super().form_valid(form)
