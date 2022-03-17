from django.shortcuts import render

# Create your views here.
def dtp_sidebar(request):
    return render(request, 'frontend/index.html')
