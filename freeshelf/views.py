from django.shortcuts import render, redirect
from freeshelf.forms import UserForm
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile

users = User.objects.all().select_related('profile')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
        return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'index.html', {'user_form': user_form})

def index(request):
    profiles = Profile.objects.all()
    return render(request, 'freeshelf/index.html', {'profiles': profiles})
