# posts/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Room, Company, UserType, Status, Profile, Booking


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')
        model = User

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        model = Company

class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        model = UserType

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        model = Status

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    userType = UserTypeSerializer()
    status = StatusSerializer()

    class Meta:
        fields = ('id', 'user', 'company', 'userType', 'status')
        model = Profile

class BookingUnrelatedSerializer(serializers.ModelSerializer):
    lead_booker = UserSerializer()
    id = serializers.IntegerField(required=False)
    room = serializers.StringRelatedField() 

    class Meta:
        fields = ('id', 'lead_booker', 'start_time', 'end_time', 'notes', 'room')
        model = Booking

    def create(self, validated_data):
        user_info = validated_data.pop('lead_booker')
        user = User.objects.get(email=user_info['email'])
        room_info = validated_data.pop('room')
        room = Room.objects.get(id=room_info['id'])
        booking = Booking.objects.create(lead_booker=user, start_time=validated_data['start_time'], end_time=validated_data['end_time'], notes=validated_data['notes'], room=room)
        return booking

class RoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    bookings = BookingUnrelatedSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'capacity', 'bookings')
        model = Room
    

    def update(self, instance, validated_data):
        booking_info = validated_data.pop('bookings')
        single_booking = booking_info[0]
        booking = Booking.objects.get(id=single_booking['id'])
        instance.bookings.add(booking)
        return instance

class BookingSerializer(BookingUnrelatedSerializer):
    room = RoomSerializer()

    class Meta:
        fields = (*BookingUnrelatedSerializer.Meta.fields, 'room')
        model = Booking