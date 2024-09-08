

# Create your views here.


    # http response 
    # return HttpResponse("Hello login details")



    # we can render or return the html for our login page instead of http response
    # 1st argument is request
    # 2nd argument is template path as string

# views.py
# views.py

# views.py (inside your login app)

from django.shortcuts import render,redirect

def user_login(request):
    
    
    return render(request, 'login_index.html')



