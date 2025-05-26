from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

# Create your views here.
def home(request):
    """
    Render the home page.
    """
    arrayOfPersons = [
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 25},
        {'name': 'Doe', 'age': 22}
    ]

    return render(request, 'home/index.html', context={'title': 'Home Page', 'persons': arrayOfPersons})
    # return HTTPResponse("Hello, World from Home!")

def successPageFromHome(request):
    """
    Render a success page from the home view.
    """
    return HTTPResponse("<h1>Success Page from Home</h1>")