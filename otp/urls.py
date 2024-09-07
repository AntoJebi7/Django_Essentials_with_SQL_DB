from django.urls import path
from . import views


urlpatterns = [
    path("", views.otpdetails ,name ="logindetails")

    
]