from django.urls import path
from . import views

app_name = 'blog'   # it means the urls are in the app name of 'blog'


urlpatterns = [
  path("",views.index,name="index"),


  # dynamic urls    number type and string type
  path("post/<str:slug>/", views.detail, name="detail"),


    #redirected scenario comes here         
    # usage : now we can able  to modify the url and it doesnt affect the url path
    #  accessibility with the help of reverse              
  path("new_modified_url", views.new_url_view, name="new_page_url"), 

    # redirected from this old url
  path("old_url", views.old_url_redirect, name="old_url"),
  path("contact", views.contact_view, name="contact"),
  

]

