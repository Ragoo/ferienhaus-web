from django import forms
from .models import Post,Trip,GuestBook,GaleryImage
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('title','text',)

class GuestbookForm(forms.ModelForm):

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