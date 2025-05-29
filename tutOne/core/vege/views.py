from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Receipe

# Create your views here.
def receipes(request):
    # data = request.POST
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')  # <-- use request.FILES here

        print({receipe_image, receipe_name, receipe_description}, ' datt')  # This will show the uploaded file objec
        # print(data, ' data from receipes view')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        # Redirect after POST to avoid CSRF issues and duplicate submissions
        return redirect('/receipes/')  # Make sure 'receipes' is the name in your urls.py

    queryset = Receipe.objects.all()

    return render(request, 'receipes.html', { 'receipesList': queryset, 'now': timezone.now() })