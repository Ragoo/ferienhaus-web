from .models import desc_text

def sidebar_processor(request):
 sidebar_text = desc_text.objects.filter(title='sidebar')
 return {'sidebar_text': sidebar_text}
