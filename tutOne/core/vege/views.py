from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Receipe

# Create your views here.
def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        print({receipe_image, receipe_name, receipe_description}, ' datt')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect('/receipes/')

    # Handle search functionality
    queryset = Receipe.objects.all()
    search_query = request.GET.get('search')
    
    if search_query:
        queryset = queryset.filter(
            receipe_name__icontains=search_query
        ) | queryset.filter(
            receipe_description__icontains=search_query
        )

    return render(request, 'receipes.html', { 'receipesList': queryset, 'now': timezone.now() })

def delete_receipe(request, id):
    """Delete a specific recipe"""
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    """Update a specific recipe"""
    receipe = get_object_or_404(Receipe, id=id)
    
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        # Update the recipe fields
        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description
        
        # Only update image if a new one is provided
        if receipe_image:
            receipe.receipe_image = receipe_image
        
        receipe.save()
        return redirect('/receipes/')
    return render(request, 'update_receipe.html', {'receipe': receipe})

def login_page(request):
    """Render the login page"""
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        # Handle registration logic here
        # For example, create a new user
        username = request.POST.get('username')

        ## password encuption
        from django.contrib.auth.hashers import make_password
        # Encrypt the password

        password = make_password(request.POST.get('password'))


        # password = request.POST.get('password')
        email = request.POST.get('email')

        # Create a new user
        if User.objects.filter(username=username).exists():
            print('Username already exists')
            return render(request, 'register.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        return redirect('/login/')
    """Render the register page"""
    return render(request, 'register.html')