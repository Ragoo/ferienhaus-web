from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import os
from location_field.models.plain import PlainLocationField


def get_image_path(instance, filename):
    return os.path.join('pictures', filename)

def get_icon_path(instance, filename):
    return os.path.join('icons', filename)

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User')
    title = models.CharField(
        max_length=200)
    text = RichTextUploadingField(config_name='full-edit')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Trip(models.Model):
    title = models.CharField(
        max_length=200)
    text = RichTextUploadingField(config_name='full-edit')

    def __str__(self):
        return self.title


class GuestBook(models.Model):
    title = models.CharField(
        max_length=200)
    author = models.CharField(
        max_length=50, blank=True, null=True)
    text = RichTextUploadingField(config_name='user-edit')
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.author + " " + str(self.created_date) + " " + self.title)


class GaleryImage(models.Model):
    title = models.CharField(
        max_length=200)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, default="")

    def __str__(self):
        return self.title


class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    text = models.CharField(max_length=30)
    details = models.CharField(max_length=50)


class desc_text(models.Model):
    title = models.CharField(
        max_length=200)
    text = RichTextUploadingField(config_name='full-edit')

    def __str__(self):
        return self.title

class markerIcon(models.Model):
    name = models.CharField(
        max_length=200)
    image = models.ImageField(upload_to=get_icon_path, default="")

    def __str__(self):
        return "<img src="+self.image.url +">"

class marker(models.Model):
    title = models.CharField(max_length=200)
    info_text = RichTextUploadingField(config_name='gmaps-edit')
    coordinates = PlainLocationField(based_fields=['city'], zoom=10, default='53.653734673045015,7.784392833709716')
    icon = models.ForeignKey(markerIcon, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title
