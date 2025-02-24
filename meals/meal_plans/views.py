from django.shortcuts import render

# Create your views here.
"""Home page view"""
def home(request):
    return render(request, 'meal_plans/home.html')