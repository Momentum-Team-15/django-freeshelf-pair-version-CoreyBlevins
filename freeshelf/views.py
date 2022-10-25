from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resources


@login_required
def index(request):
    resources = Resources.objects.all()
    return render(request, 'freeshelf/index.html', {'resources': resources})

def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')


