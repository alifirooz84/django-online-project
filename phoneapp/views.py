from django.shortcuts import render, redirect
from .forms import PhoneNumberForm

def phone_input(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = PhoneNumberForm()
    return render(request, 'phone_input.html', {'form': form})

