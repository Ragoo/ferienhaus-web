from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ferienhausWeb/home.html', {'posts': posts})

def ferienhaus(request):
    return render(request, 'ferienhausWeb/ferienhaus.html', {})

def ferienhaus_galerie(request):
    return render(request, 'ferienhausWeb/ferienhaus_galerie.html', {})

def belegugnskalender(request):
    return render(request, 'ferienhausWeb/belegugnskalender.html', {})