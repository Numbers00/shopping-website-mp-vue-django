from django.urls import path

from user import views

urlpatterns = [
    path('user-details/', views.UserViewSet),
    path('send_confirmation_email/', views.send_confirmation_email, name='send_confirmation_email'),
]