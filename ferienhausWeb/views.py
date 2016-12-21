from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm,TripForm,GuestbookForm,GaleryImageForm
from datetime import date, datetime, timedelta
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from .models import *



# Create your views here.

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ferienhausWeb/home.html', {'posts': posts})


def ferienhaus(request):
    return render(request, 'ferienhausWeb/ferienhaus.html', {})


def ferienhaus_galerie(request):
    galeryimage = GaleryImage.objects.order_by('title')
    return render(request, 'ferienhausWeb/ferienhaus_galerie.html', {'galeryimage': galeryimage})


def belegungskalender(request):
    return render(request, 'ferienhausWeb/belegungskalender.html', {})


def umgebung(request):
    trips = Trip.objects.order_by('title')
    return render(request, 'ferienhausWeb/umgebung.html', {'trips': trips})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trips = Trip.objects.order_by('title')
    return render(request, 'ferienhausWeb/trip_detail.html', {'trip': trip, 'trips': trips})


def guestbook(request):
    guestbook_entries = GuestBook.objects.order_by('-created_date')
    if request.method == "POST":
        form = GuestbookForm(request.POST)
        if form.is_valid():
            guestbook = form.save(commit=False)
            guestbook.published_date = timezone.now()
            guestbook.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm()
    return render(request, 'ferienhausWeb/gaestebuch.html', {'guestbook_entries': guestbook_entries, 'form': form})


"""
Post create, edit, delete
"""
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'ferienhausWeb/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'ferienhausWeb/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

@login_required
def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('trip_detail',pk=trip.pk)
    else:
        form = TripForm()
    return render(request, 'ferienhausWeb/trip_edit.html', {'form': form})

@login_required
def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('trip_detail',pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'ferienhausWeb/trip_edit.html', {'form': form})

@login_required
def trip_remove(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return redirect('umgebung')

@login_required
def guestbook_remove(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    guestbook.delete()
    return redirect('guestbook')

def galeryimage_new(request):
    if request.method == "POST":
        form = GaleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect('ferienhaus_galerie')
    else:
        form = GaleryImageForm()
    return render(request, 'ferienhausWeb/galeryimage_edit.html', {'form': form})

@login_required
def galeryimage_remove(request, pk):
    galeryimage = get_object_or_404(GaleryImage, pk=pk)
    galeryimage.delete()
    return redirect('ferienhaus_galerie')

#Calendar

def eventsXML(request):
    eventList = Event.objects.all()
    return render_to_response('events.xml',
                              {'eventList': eventList},
                              content_type="application/xhtml+xml")


@csrf_exempt
def dataprocessor(request):
    responseList = []

    if request.method == 'POST':

        command = request.POST['!nativeeditor_status']

        if command == 'inserted':
            e = Event()
            e.start_date = request.POST['start_date']
            e.end_date = request.POST['end_date']
            e.text = request.POST['text']
            e.details = ' '
            e.save()
            response = {'type': 'insert',
                        'sid': request.POST['id'],
                        'tid': e.id}

        elif command == 'updated':
            e = Event(pk=request.POST['id'])
            e.start_date = request.POST['start_date']
            e.end_date = request.POST['end_date']
            e.text = request.POST['text']
            e.details = ' '
            e.save()
            response = {'type': 'update',
                        'sid': e.id,
                        'tid': e.id}


        elif command == 'deleted':
            e = Event(pk=request.POST['id'])
            e.delete()
            response = {'type': 'delete',
                        'sid': request.POST['id'],
                        'tid': '0'}

        else:
            response = {'type': 'error',
                        'sid': request.POST['id'],
                        'tid': '0'}

        responseList.append(response)

    return render_to_response('dataprocessor.xml', {"responseList": responseList},
                              content_type="application/xhtml+xml")
