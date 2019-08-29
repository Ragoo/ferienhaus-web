# coding=utf-8
from django import forms
from .models import Post,Trip,GuestBook,GaleryImage,desc_text,markerIcon,marker
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from captcha.fields import ReCaptchaField

class CustomChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return mark_safe(" %s <br/> <img src='%s'/>" % (obj.name, obj.image.url))

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('title','text',)

class GuestbookForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = GuestBook
        fields = ('author','title','text',)
        labels = {
            'author': ('Name'),
            'title': ('Überschrift'),
        }

class GaleryImageForm(forms.ModelForm):

    class Meta:
        model = GaleryImage
        fields = ('title','text','image',)

class TextForm(forms.ModelForm):

    class Meta:
        model = desc_text
        fields = ('text',)

class MarkerIconForm(forms.ModelForm):

    class Meta:
        model = markerIcon
        fields = ('name','image',)

class MarkerForm(forms.ModelForm):
    icon = CustomChoiceField(widget=forms.RadioSelect(renderer=HorizRadioRenderer), queryset=markerIcon.objects.all())

    class Meta:
        model = marker
        fields = ('title','info_text','coordinates','icon','zIndex')
        labels = {
            'title': ('Titel'),
            'info_text': ('Beschreibung'),
            'coordinates': ('Koordinaten (Karte nutzen)'),
            'icon': ('Icon'),
            'zIndex': ('zIndex - zwischen 1 und 999 (umso höher der Wert, umso höher ist der Marker über anderen Markern)'),
        }