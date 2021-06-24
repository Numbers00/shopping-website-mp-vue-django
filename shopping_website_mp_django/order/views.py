from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('book').price for item in serializer.validated_data['items'])

        serializer.save(user=request.user, paid_amount=paid_amount)

        send_email(request, paid_amount)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_email(request, paid_amount):
    print(request)

    order = Order.objects.filter(user=request.user)[0]
    order_serializer = MyOrderSerializer(order)

    template = render_to_string(
            'base/email_template.html', 
            {
                'full_name': request.data['full_name'], 
                'address': request.data['address'], 
                'phone': request.data['phone'], 
                'paid_amount': paid_amount,
                'order': order_serializer.data
                }
            )

    email = EmailMessage(
        "Thank you for your purchase at Code & Chill",
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )

    email.fail_silently = False
    email.send()

    return Response('', status=status.HTTP_201_CREATED)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)