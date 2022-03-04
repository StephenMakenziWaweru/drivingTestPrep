from django.views.generic import ListView
from django.shortcuts import render
from .models import Sign

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'highwaysign/home.html')

def signs(request):
    """Signs homepage"""
    return render(request, 'highwaysign/highwaysigns.html')

class ClassASignsListView(ListView):
    """Class A Highway Signs"""
    model = Sign
    template_name = 'highwaysign/class_a_signs.html'
    context_object_name = 'signs_list'

class ClassBSignsListView(ListView):
    """Class B Highway Signs"""
    model = Sign
    template_name = 'highwaysign/class_b_signs.html'
    context_object_name = 'signs_list'

class ClassCSignsListView(ListView):
    """Class C Highway Signs"""
    model = Sign
    template_name = 'highwaysign/class_c_signs.html'
    context_object_name = 'signs_list'
