from django.urls import path
from . import views


#create urls.py within the app and create a list called urlpatterns=[] and initialize the path

urlpatterns = [

    #path()
    # to root url ""
    # 1st parameter determines whats is in " url path"
    # 2nd parameter determines what to do with the url  and also import modules as needed
    # 3rd parameter determines the name
    # it returns the http response 

      #   path("", views.logindetails ,name ="logindetails")

    # we need the feed this url to main project directory (myapp -> urls.py -> )


    # we can render or return the html for our login page instead of http response
    path("", views.logindetails ,name ="logindetails")



    
]
