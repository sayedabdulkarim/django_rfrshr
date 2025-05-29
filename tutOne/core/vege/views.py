from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

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