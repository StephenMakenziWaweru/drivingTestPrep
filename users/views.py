from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from questions.models import Question
from mtb.models import Video, Notes


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'User exists!')
            form = UserRegisterForm()
            return render(request, 'users/register.html', {'form': form})

    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # quiz = get_object_or_404(Question)
    quiz = Question.objects.filter(qs_owner=request.user)
    video = Video.objects.filter(owner=request.user)
    note = Notes.objects.filter(owner=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid:
            u_form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {'u_form': u_form, 
                'quiz_count': quiz.count(),
                'video_count': video.count(),
                'note_count': note.count(),
                }

    return render(request, 'users/profile.html', context=context)
