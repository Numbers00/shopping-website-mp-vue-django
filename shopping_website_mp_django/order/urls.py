from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('send_email/', views.send_email, name='send_email'),
    path('orders/', views.OrdersList.as_view())
]