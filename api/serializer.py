from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from galleryapp.models import Gallery

class GallerySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"