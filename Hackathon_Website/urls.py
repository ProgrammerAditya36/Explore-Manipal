from django.template.context_processors import static

from . import views, settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import  views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restaurant/', include('restaurant.urls')),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name='reset-password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete")

]
urlpatterns += static(settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL)
