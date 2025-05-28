from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def receipes(request):
    return render(request, 'receipes.html', { 'now': timezone.now() })