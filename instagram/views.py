from django.shortcuts import render
from .models import Image
# Create your views here.




def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'home.html', context)