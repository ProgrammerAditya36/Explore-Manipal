from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from events.models import User_Events
from restaurant.models import Review
from .forms import CustomUserCreationForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from events.models import User_Events

# Create your views here.
def profiles(request):
    profiles_ = Profile.objects.all()
    context = {"profiles":profiles_}
    return render(request, 'users/profiles.html',context)



def logoutUser(request):
    logout(request)
    messages.error(request, 'User Was logged out')
    return redirect('login')


def profile(request, user_id):
    # Get the user object using the user_id
    user = get_object_or_404(User, id=user_id)

    # Check if the user has a profile
    if hasattr(user, 'profile'):
        # Retrieve events associated with the user's profile
        events = User_Events.objects.filter(profile=user.profile)
        reviews = Review.objects.filter(by=user.profile)
    else:
        events = []
        reviews = []

    context = {"profile": user.profile, "events": events, "reviews":reviews}
    return render(request, 'users/profile.html', context)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except :
            messages.error(request,'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password Incorrect')
    context = {'page':page}
    return render(request, 'users/login_register.html',context)
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return  redirect('edit-account')
        else:
            messages.success(request, 'An error has occurred')
    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile_ = request.user.profile
    form = ProfileForm(instance=profile_)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_)
        if form.is_valid():
            form.save()

            # Reverse the 'profile' URL with the 'user_id' argument
            profile_url = reverse('profile', kwargs={'user_id': request.user.id})
            return redirect(profile_url)

    context ={'form':form}
    return render(request, 'users/profile_form.html', context)

