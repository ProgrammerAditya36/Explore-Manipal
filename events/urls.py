from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('adduserevent/',views.createUserEvent,name='add-user-event'),
    path('updateuserevent/<str:event_id>', views.updateUserEvent, name='update-user-event'),
    path('deleteuserevent/<str:event_id>', views.deleteUserEvent, name='delete-user-event')
]
