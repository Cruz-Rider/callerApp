# Views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.urls import reverse

from .serializers import *
from .models import *

class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'registration': reverse('register', request=request, format=format),
            'search': reverse('search', request=request, format=format),
        })


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisteredUserSerializer

    def create(self, request):
        password = request.data.get('password', None)
        phone_number = request.data.get('phone_number', None)
        
        if not password:
            return Response({'password': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        elif not phone_number:
            return Response({'password': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_model().objects.create_user(
            username=request.data['username'],
            password=password,
            email=request.data.get('email', ''),
            phone_number=phone_number,
            first_name=request.data.get('first_name', ''),
            last_name=request.data.get('last_name', '')
        )

        serializer = self.get_serializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
class RegisteredUserView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class SearchView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_param = request.query_params.get('Search')

        registered = RegisteredUser.objects.filter(first_name__icontains=query_param) or \
                      RegisteredUser.objects.filter(phone_number__icontains=query_param)
        unregistered = Contacts.objects.filter(first_name__icontains=query_param) or \
                      Contacts.objects.filter(phone_number__icontains=query_param)

        if registered.exists():
            results = registered
            serializer = RegisteredUserSerializer(results, many=True)
            data = []

            for registered_user in results:
                user_data = {
                    'name': registered_user.first_name + ' ' + registered_user.last_name,
                    'phone_number': registered_user.phone_number,
                    'email': registered_user.email
                }
                data.append(user_data)

            return Response(data)
        elif unregistered.exists():
            results = unregistered
            serializer = RegisteredUserSerializer(results, many=True)
            data = []

            for unregistered_user in results:
                user_data = {
                    'name': unregistered_user.first_name + ' ' + unregistered_user.last_name,
                    'phone_number': unregistered_user.phone_number,
                    'spam': unregistered_user.is_spam
                }
                data.append(user_data)

            return Response(data)
        else:
            return Response({'NoData': "No data found for this search!"})