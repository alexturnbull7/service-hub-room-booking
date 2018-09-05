from django.shortcuts import render

# Create your views here.

# posts/views.py
from rest_framework import generics
from rest_framework.decorators import action

from django.contrib.auth.models import User

from .models import Room, Company, UserType, Status, Profile, Booking
from .serializers import UserSerializer, RoomSerializer, CompanySerializer, UserTypeSerializer, StatusSerializer, ProfileSerializer, BookingSerializer
from dateutil import parser

from datetime import datetime

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserTypeList(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class UserTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class RoomSearchList(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        all_rooms = Room.objects.all()
        startTime = self.request.query_params.get('startTime', None)
        endTime = self.request.query_params.get('endTime', None)
        startDt = parser.parse(startTime)
        endDt = parser.parse(endTime)

        filtered = Room.objects.filter(bookings__start_time__lte=endDt, bookings__end_time__gte=startDt)
        final = [x for x in all_rooms if x not in filtered]
        
        return final

class BookingByLeadBooker(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        lead_booker_id = self.request.query_params.get('lead_booker_id', None)
        filtered = Booking.objects.filter(lead_booker__id=lead_booker_id)
        return filtered
