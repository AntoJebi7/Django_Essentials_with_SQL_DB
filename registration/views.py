# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('/')  # Redirect to login or home after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'index_register.html', {'form': form})

