from django.shortcuts import render, redirect
from .models import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  ProfileUpdateForm
# Create your views here.




def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'home.html', context)


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
           
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
       
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
    