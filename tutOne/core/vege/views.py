from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
    if request.method == "POST":
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        print(username_or_email, password, 'login data')

        # Validate required fields
        if not username_or_email or not password:
            messages.error(request, 'Username/Email and password are required.')
            return render(request, 'login.html')

        # Try to find user by username or email
        user = None
        if User.objects.filter(username=username_or_email).exists():
            user = authenticate(request, username=username_or_email, password=password)
        elif User.objects.filter(email=username_or_email).exists():
            user_obj = User.objects.filter(email=username_or_email).first()  # Use first() instead of get()
            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/receipes/')
        else:
            messages.error(request, 'Invalid username/email or password.')
    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        # Handle registration logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Validate required fields
        if not username or not password or not email:
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'register.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return render(request, 'register.html')

        try:
            # Create a new user (Django handles password hashing automatically)
            user = User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, 'An error occurred during registration. Please try again.')
            return render(request, 'register.html')
    
    """Render the register page"""
    return render(request, 'register.html')