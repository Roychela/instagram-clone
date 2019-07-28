from django.shortcuts import render, redirect
from .models import Image, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  ProfileUpdateForm, ImageForm
# Create your views here.




def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'home.html', context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
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

    return render(request, 'update_profile.html', context)

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')  
def upload_image(request):
    user = request.user
    print(user)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = user
            image.save()
            print(image.user)
            return redirect('blog-home')
    else:
        form = ImageForm()
    return render(request, "upload_image.html", {"form":form})