from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b

def say_hello(request):
    x = calculate_sum(5, 3)
    rendered_template = render(request, 'hello.html', { 
        'greeting': 'Hello, world! This is the playground app. The sum of 5 and 3 is: ' + str(x),
        'name': 'Playground User, the sum of 5 and 3 is: ' + str(x)
    })
    return rendered_template

def home(request):
    return HttpResponse("Welcome to the Playground app! This is a simple view.")
    # return HttpResponse("Hello, world! This is the playground app.")