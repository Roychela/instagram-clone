from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Profile, Comments, Follow
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  ProfileUpdateForm, ImageForm, CommentForm
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.



@login_required(login_url='/accounts/login/')
def home(request):
    context = {
        'images': Image.objects.all(),
        'comments': Comments.objects.all()
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


def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    user_profile = User.objects.get(username=current_user)
    comments = Comments.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.commenter = current_user
            comment.save()

            print(comments)


        return redirect(home)

    else:
        form = CommentForm()

    return render(request, 'comments.html', locals())

@login_required(login_url='/accounts/login/')
def user_profile(request, id):
    user=User.objects.filter(id=id).first()
    profile = user.profile
    profile_details = Profile.get_profile_id(id)
    images = Image.get_profile_images(id)
    return render(request,'profile.html',locals())
@login_required(login_url='/accounts/login/')
def like(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    request.user.profile.like(image)
    return JsonResponse(image.total_likes, safe=False)

@login_required(login_url='/accounts/login/')
def unlike(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    request.user.profile.unlike(image)
    return JsonResponse(image.total_likes, safe=False)


def follow(request, following_id):
    current_user = request.user
    trial = User.objects.get(username=current_user).pk
    if request.method == 'POST':
        trial_id = current_user.id
        new_follower = Follow.objects.create(user_id=trial, following_id=following_id)
    return redirect(home)

