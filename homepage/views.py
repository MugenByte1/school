from django.shortcuts import render
from .models import HomePage

def home(request):
    homepage = HomePage.objects.first()
    return render(request, 'homepage/home.html', {'homepage': homepage})
