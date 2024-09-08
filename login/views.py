from django.shortcuts import render, redirect
from django.contrib import messages
from registration.models import Registration

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        print(f"Attempting login:")
        print(f"Username: {username}")
        print(f"Password: {raw_password}")

        try:
            # Fetch the user by username from the Registration model
            user = Registration.objects.get(username=username)
            print(f"User found: {user.username}")
            print(f"Stored password: {user.password}")

            # Check if the password matches directly
            if user.password == raw_password:
                print(f"Password is correct for user: {user.username}")
                # Successful login: redirect to the blog page
                return redirect('/blog')  # Ensure '/blog' is the correct URL path for your blog page
            else:
                print("Password does not match")
                messages.error(request, 'Invalid password')

        except Registration.DoesNotExist:
            print("Username does not exist")
            messages.error(request, 'Username does not exist')

    return render(request, 'login_index.html')

































# Create your views here.


    # http response 
    # return HttpResponse("Hello login details")



    # we can render or return the html for our login page instead of http response
    # 1st argument is request
    # 2nd argument is template path as string

# views.py
# views.py

# views.py (inside your login app)

# Import the Registration model from the 'registration' app
# In authentication/views.py