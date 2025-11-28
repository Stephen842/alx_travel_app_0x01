from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for managing property listings.
    offers full CRUD operations: list, retrieve, create, update, delete
    '''
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    authentication_class = [TokenAuthentication, SessionAuthentication]
    permission_class = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for managing bookings.
    offers full CRUD operations: list, retrieve, create, update, delete
    '''
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_class = [TokenAuthentication, SessionAuthentication]
    permission_class = [IsAuthenticated]