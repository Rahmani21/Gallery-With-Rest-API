from django.shortcuts import render
from rest_framework import viewsets
from api.serializer import GallerySerialzer
from rest_framework.permissions import IsAdminUser
from galleryapp.models import Gallery

# Create your views here.



class Galleryapi(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerialzer
    permission_classes = [IsAdminUser]
    
