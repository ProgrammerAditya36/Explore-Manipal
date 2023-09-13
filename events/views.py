from django.shortcuts import render, redirect, get_object_or_404
from events.models import Events,User_Events
from .forms import UserEventAdd
from django.contrib.auth.decorators import login_required
from users.models import Profile
# Create your views here.
def events(request):
    events_ = Events.objects.order_by('date').reverse()
    user_events_ = User_Events.objects.order_by('date')
    context = {'events':events_,'user_events':user_events_}
    return render(request, 'events/events.html', context=context)


@login_required(login_url='register')
def createUserEvent(request):
    if request.method == "POST":
        user_event_form = UserEventAdd(request.POST, request.FILES)
        if user_event_form.is_valid():
            user_event = user_event_form.save(commit=False)
            user_event.user = request.user
            try:
                profile = request.user.profile
                user_event.profile = profile
            except Profile.DoesNotExist:
                pass
            user_event.save()
            return redirect('events')
    else:
        user_event_form = UserEventAdd()

    context = {'user_event': user_event_form}
    return render(request, 'events/add_events.html', context)


@login_required(login_url='register')
def updateUserEvent(request, event_id):
    user_event = get_object_or_404(User_Events, id=event_id, profile=request.user.profile)

    if request.method == "POST":
        user_event_form = UserEventAdd(request.POST, request.FILES, instance=user_event)
        if user_event_form.is_valid():
            user_event = user_event_form.save()
            return redirect('events')
    else:
        user_event_form = UserEventAdd(instance=user_event)

    context = {'user_event': user_event_form}
    return render(request, 'events/update_event.html', context)


@login_required(login_url='register')
def deleteUserEvent(request, event_id):
    profile = request.user.profile
    user_event = get_object_or_404(User_Events, id=event_id,profile=profile)

    if request.method == "POST":
        user_event.delete()
        return redirect('events')

    context = {'user_event': user_event, 'profile':profile}
    return render(request, 'delete_template.html', context)