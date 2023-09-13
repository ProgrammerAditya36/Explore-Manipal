import os
import django
from restaurant.models import Restaurant, Review,Image,Facility
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from events.models import Events, User_Events
from django.db.models import Q
from .forms import ReviewAdd, RestaurantFilterForm, RestaurantAddForm, ImageUploadForm, CustomFacilityForm
from django.contrib.auth.decorators import login_required
from .models import Facility, DayOpen


# Create your views here.
def restaurants(request):
    search_query = request.GET.get('search_query', '')
    selected_facilities = request.GET.getlist('facilities')
    selected_open_days = request.GET.getlist('open_days')
    facilities = Facility.objects.all()
    open_days = DayOpen.objects.all()
    # Initialize the filter form
    filter_form = RestaurantFilterForm(request.GET)

    restaurants_ = Restaurant.objects.distinct().filter(
        Q(name__icontains=search_query)
    )

    if selected_facilities:
        restaurants_ = restaurants_.filter(facilities__in=selected_facilities)
    if selected_open_days:
        restaurants_ = restaurants_.filter(open_days__in=selected_open_days)
    context = {'restaurants': restaurants_, 'search_query': search_query, 'filter_form': filter_form,
               'facilities': facilities, 'open_days': open_days}
    return render(request, 'restaurant/restaurants.html', context)


@login_required(login_url='register')
def restaurant(request, pk):
    restaurant_ = Restaurant.objects.get(id=pk)
    reviews = Review.objects.filter(project__id=pk)
    images_ = restaurant_.images.all()

    if request.method == "POST":
        add_review_form = ReviewAdd(request.POST)
        if add_review_form.is_valid():
            user_event = add_review_form.save(commit=False)
            user_event.by = request.user.profile  # Set the review's 'by' field to the user's profile
            user_event.project = restaurant_  # Set the review's 'project' field to the restaurant
            user_event.save()
            return redirect('restaurant', pk=pk)  # Redirect to the same restaurant page

    else:
        add_review_form = ReviewAdd()

    context = {'restaurant': restaurant_, 'images': images_, 'reviews': reviews, 'add_review': add_review_form}
    return render(request, 'restaurant/single_restaurant.html', context)


@login_required(login_url='register')
def updateReviews(request, review_id):
    user_event = get_object_or_404(Review, id=review_id, by=request.user.profile)

    if request.method == "POST":
        user_event_form = ReviewAdd(request.POST, request.FILES, instance=user_event)
        if user_event_form.is_valid():
            user_event = user_event_form.save()
            return redirect('restaurants')
    else:
        user_event_form = ReviewAdd(instance=user_event)

    context = {'user_event': user_event_form}
    return render(request, 'restaurant/update_review.html', context)


@login_required(login_url='register')
def deleteReview(request, review_id):
    profile = request.user.profile
    user_event = get_object_or_404(Review, id=review_id, by=profile)

    if request.method == "POST":
        user_event.delete()
        return redirect('restaurants')

    context = {'user_event': user_event, 'profile': profile}
    return render(request, 'delete_template.html', context)


def restaurant_add_facilities(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)

    if request.method == "POST":
        facility_form = CustomFacilityForm(request.POST)
        image_upload_form = ImageUploadForm(request.POST, request.FILES)

        if facility_form.is_valid():
            # Process user-added facilities and associate them with the restaurant
            facility_name = facility_form.cleaned_data['facility_name']
            restaurant.facilities.create(name=facility_name)

        if image_upload_form.is_valid():
            # Process the uploaded image and associate it with the restaurant
            image_data = image_upload_form.cleaned_data['image']
            restaurant.images.create(image=image_data)

    else:
        facility_form = CustomFacilityForm()
        image_upload_form = ImageUploadForm()

    context = {
        'facility_form': facility_form,
        'image_upload_form': image_upload_form,
        'restaurant': restaurant,
    }
    return render(request, 'restaurant/restaurant_add_facilities.html', context)

def restaurant_add(request):
    if request.method == "POST":
        form = RestaurantAddForm(request.POST, request.FILES)

        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_add_facilities', pk=restaurant.pk)
    else:
        form = RestaurantAddForm()

    context = {'form': form}
    return render(request, 'restaurant/restaurant_add.html', context)

def homepage(request):
    return render(request, 'index.html')
