from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def send_confirmation_email(request):
    print(request.data)

    template = render_to_string(
            'base/confirmation_email_template.html', 
            {
                'full_name': request.data['full_name'], 
                'email': request.data['email'], 
                'address': request.data['address'],
                'phone': request.data['phone']
                }
            )

    email = EmailMessage(
        "Thank you signing up at Code & Chill",
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )

    email.fail_silently = False
    email.send()

    return Response('', status=status.HTTP_201_CREATED)







# from django.shortcuts import render

# from django.http import JsonResponse

# from rest_framework import status, authentication, permissions
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response

# @api_view(['GET'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
# def user_view(request):
#     if request.user.is_authenticated():
#         return JsonResponse({"full_name": request.user.full_name, "email": request.user.email,  "address": request.user.address, "phone": request.user.phone})

#     return Response(status=status.HTTP_400_BAD_REQUEST)