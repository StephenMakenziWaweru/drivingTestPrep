from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Question
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
@login_required
def likeView(request, pk):
    """Track likes"""
    quiz = get_object_or_404(Question, id=request.POST.get('quiz_id'))
    quiz.qs_likes.add(request.user)
    quiz.qs_dislikes.remove(request.user)
    return HttpResponseRedirect(reverse('general-q'))

@login_required
def dislikeView(request, pk):
    """Track likes"""
    quiz = get_object_or_404(Question, id=request.POST.get('quiz_id'))
    quiz.qs_dislikes.add(request.user)
    quiz.qs_likes.remove(request.user)
    return HttpResponseRedirect(reverse('general-q'))

class GeneralListView(LoginRequiredMixin, CreateView, ListView):
    """General questions"""
    model = Question
    template_name = 'questions/general_questions.html'
    context_object_name = 'quiz_list'
    fields = ['qs_title', 'qs_answer', 'qs_type']
    paginate_by = 10
    
    def form_valid(self, form):
        form.instance.qs_owner = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Question.objects.filter(qs_type='General')

    def get_context_data(self, **kwargs):
        # Kinda long but works for me
        # get context data first
        # for each object in the list fetch likes count using id
        # insert a key value in each of the objects dict corresponding
        #  to no. of likes 
        context = super().get_context_data(**kwargs) 
        for index, quiz in enumerate(context['quiz_list']):
            total_likes = get_object_or_404(Question, id=quiz.id).total_likes()
            total_dislikes = get_object_or_404(Question, id=quiz.id).total_dislikes()
            context['quiz_list'][index].__dict__['total_likes'] = total_likes
            context['quiz_list'][index].__dict__['total_dislikes'] = total_dislikes
        # for quiz in context['quiz_list']:
        #     print(quiz.total_likes)
        return context


class DefinitionsListView(LoginRequiredMixin, CreateView, ListView):
    """Definition questions"""
    model = Question
    template_name = 'questions/definition_questions.html'
    context_object_name = 'quiz_list'
    fields = ['qs_title', 'qs_answer', 'qs_type']
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Definition')

class SignsListView(LoginRequiredMixin, CreateView, ListView):
    """Signs questions"""
    model = Question
    template_name = 'questions/sign_questions.html'
    context_object_name = 'quiz_list'
    fields = ['qs_title', 'qs_answer', 'qs_type']
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Signs')

class MtbListView(LoginRequiredMixin, CreateView, ListView):
    """mtb questions Signs"""
    model = Question
    template_name = 'questions/mtb_questions.html'
    context_object_name = 'quiz_list'
    fields = ['qs_title', 'qs_answer', 'qs_type']
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Mtb')

class QuestionDetailView(DetailView):
    """Question detailed view"""
    model = Question
    template_name = 'questions/question_detail.html'


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Question"""
    model = Question
    template_name = 'questions/question_edit.html'
    fields = ['qs_title', 'qs_type', 'qs_answer']
    

    def form_valid(self, form):
        form.instance.qs_owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().qs_owner:
            return True
        return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Edit Question"""
    model = Question
    template_name = 'questions/question_delete.html'
    success_url = reverse_lazy('general-q')

    def test_func(self):
        if self.request.user == self.get_object().qs_owner or self.request.user == 'admin':
            return True
        return False

