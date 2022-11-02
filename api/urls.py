
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("galleryapi", views.Galleryapi, "categoryapi")



app_name = "api"
urlpatterns = [

    path("",include(router.urls))


] 

