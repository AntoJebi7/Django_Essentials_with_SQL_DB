from django.shortcuts import render # to render html
from django.http import HttpResponse

# Create your views here.
def logindetails(request):

    # http response 
    # return HttpResponse("Hello login details")



    # we can render or return the html for our login page instead of http response
    # 1st argument is request
    # 2nd argument is template path as string

    return render(request,'login_index.html')

