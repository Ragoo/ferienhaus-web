from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm,TripForm,GuestbookForm,GaleryImageForm,TextForm,MarkerForm,MarkerIconForm
from datetime import date, datetime, timedelta
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.

def home(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    texts = desc_text.objects.filter(title='home')
    paginator = Paginator(post_list, 3)  # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'ferienhausWeb/home.html', {'posts': posts, 'texts':texts})


def ferienhaus(request):
    texts = desc_text.objects.filter(title='ferienhaus_desc')
    return render(request, 'ferienhausWeb/ferienhaus.html', {'texts':texts})


def ferienhaus_galerie(request):
    galeryimage = GaleryImage.objects.order_by('title')
    return render(request, 'ferienhausWeb/ferienhaus_galerie.html', {'galeryimage': galeryimage})

def preise(request):
    texts = desc_text.objects.filter(title='preise')
    return render(request, 'ferienhausWeb/preise.html', {'texts':texts})


def belegungskalender(request):
    return render(request, 'ferienhausWeb/belegungskalender.html', {})


def umgebung(request):
    trips = Trip.objects.order_by('title')
    markers = marker.objects.all()
    markericons = markerIcon.objects.all()
    return render(request, 'ferienhausWeb/umgebung.html', {'trips': trips,'markers':markers,'markericons':markericons})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trips = Trip.objects.order_by('title')
    return render(request, 'ferienhausWeb/trip_detail.html', {'trip': trip, 'trips': trips})


def guestbook(request):
    #guestbook_entries = GuestBook.objects.order_by('-created_date')
    guestbook_list = GuestBook.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(guestbook_list, 3)  # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        guestbook_entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        guestbook_entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        guestbook_entries = paginator.page(paginator.num_pages)
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

"""
Trip create, edit, delete (Umgebung)
"""

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

@login_required
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


@login_required
def markericon_list(request):
    markericons = markerIcon.objects.order_by('name')
    markers = marker.objects.order_by('icon')
    trips = Trip.objects.order_by('title')
    if request.method == "POST":
        form = MarkerIconForm(request.POST, request.FILES)
        if form.is_valid():
            marker_icon = form.save(commit=False)
            marker_icon.save()
            return redirect('markericon_list')
    else:
        form = MarkerIconForm()
    return render(request, 'ferienhausWeb/markericon_list.html', {'trips': trips,'markers': markers,'markericons': markericons, 'form':form})

@login_required
def markericon_remove(request, pk):
    markericon_ = get_object_or_404(markerIcon, pk=pk)
    markericon_.delete()
    return redirect('markericon_list')

@login_required
def markericon_edit(request, pk):
    markericon_ = get_object_or_404(markerIcon, pk=pk)
    markers = marker.objects.order_by('icon')
    markericons = markerIcon.objects.all()
    trips = Trip.objects.order_by('title')
    if request.method == "POST":
        form = MarkerIconForm(request.POST, instance=markericon_)
        if form.is_valid():
            markericon_ = form.save(commit=False)
            markericon_.save()
            return redirect('markericon_list')
    else:
        form = MarkerIconForm(instance=markericon_)
    return render(request, 'ferienhausWeb/markericon_list.html', {'trips': trips,'markers': markers,'form': form, 'markericons':markericons})

@login_required
def marker_list(request):
    markers = marker.objects.order_by('icon')
    trips = Trip.objects.order_by('title')
    markericons = markerIcon.objects.all()
    if request.method == "POST":
        form = MarkerForm(request.POST)
        if form.is_valid():
            marker_ = form.save(commit=False)
            marker_.save()
            return redirect('marker_list')
    else:
        form = MarkerForm()
    return render(request, 'ferienhausWeb/marker_list.html', {'trips': trips,'markers': markers, 'form':form, 'markericons':markericons})

@login_required
def marker_remove(request, pk):
    marker_ = get_object_or_404(marker, pk=pk)
    marker_.delete()
    return redirect('marker_list')

@login_required
def marker_edit(request, pk):
    marker_ = get_object_or_404(marker, pk=pk)
    markers = marker.objects.order_by('icon')
    markericons = markerIcon.objects.all()
    trips = Trip.objects.order_by('title')
    if request.method == "POST":
        form = MarkerForm(request.POST, instance=marker_)
        if form.is_valid():
            marker_ = form.save(commit=False)
            marker_.save()
            return redirect('marker_list')
    else:
        form = MarkerForm(instance=marker_)
    return render(request, 'ferienhausWeb/marker_list.html', {'trips': trips,'markers': markers,'form': form, 'markericons':markericons})


@login_required
def text_edit(request, pk):
    text = get_object_or_404(desc_text, pk=pk)
    if request.method == "POST":
        form = TextForm(request.POST, instance=text)
        if form.is_valid():
            text = form.save(commit=False)
            text.save()
            return redirect('home')
    else:
        form = TextForm(instance=text)
    return render(request, 'ferienhausWeb/text_edit.html', {'form': form})

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
