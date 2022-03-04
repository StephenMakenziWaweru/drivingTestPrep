from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import Question
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def likeView(request, pk):
    """Track likes"""
    quiz = get_object_or_404(Question, id=request.POST.get('quiz_id'))
    quiz.qs_likes.add(request.user)
    return HttpResponseRedirect(reverse('general-q'))

class GeneralListView(ListView):
    """General questions"""
    model = Question
    template_name = 'questions/general_questions.html'
    context_object_name = 'quiz_list'
    paginate_by = 10
    
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
            context['quiz_list'][index].__dict__['total_likes'] = total_likes
        # for quiz in context['quiz_list']:
        #     print(quiz.total_likes)
        return context


class DefinitionsListView(ListView):
    """Definition questions"""
    model = Question
    template_name = 'questions/definition_questions.html'
    context_object_name = 'quiz_list'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Definition')

class SignsListView(ListView):
    """Signs questions"""
    model = Question
    template_name = 'questions/sign_questions.html'
    context_object_name = 'quiz_list'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Signs')

class MtbListView(ListView):
    """mtb questions Signs"""
    model = Question
    template_name = 'questions/mtb_questions.html'
    context_object_name = 'quiz_list'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(qs_type='Mtb')
