from django.contrib import admin
from .models import Post, Trip,GuestBook,GaleryImage,Event,desc_text

admin.site.register(Post)
admin.site.register(Trip)
admin.site.register(GuestBook)
admin.site.register(GaleryImage)
admin.site.register(Event)
admin.site.register(desc_text)