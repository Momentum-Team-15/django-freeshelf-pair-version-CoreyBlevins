from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    profiles = User.objects.all()
    return render(request, 'freeshelf/index.html', {'profiles': profiles})
