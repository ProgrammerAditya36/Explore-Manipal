from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('add-restaurant/',views.restaurant_add, name='add-restaurant'),
    path('update-review/<str:review_id>',views.updateReviews, name="update-review"),
    path('add-facilities/<uuid:pk>/', views.restaurant_add_facilities, name='restaurant_add_facilities'),
    path('delete-review/<str:review_id>', views.deleteReview, name="delete-review"),
    path('<str:pk>/',views.restaurant,name="restaurant"),

]
