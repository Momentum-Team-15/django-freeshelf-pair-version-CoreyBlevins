from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resources
from freeshelf.forms import ResourceForm


@login_required
def index(request):
    resources = Resources.objects.all()
    return render(request, 'freeshelf/index.html', {'resources': resources})

def resource_detail(request, pk):
    resource = Resources.objects.get(pk=pk)
    return render(request, 'freeshelf/resource_detail.html', {'resource': resource})

def edit_resources(request, pk):
    edit = get_object_or_404(Resources, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('resource_detail', pk=edit.pk)
    else:
        form = ResourceForm(instance=edit)
    return render(request, 'freeshelf/edit_resource.html', {'form': form})

def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResourceForm()
    return render(request, 'freeshelf/create_resource.html', {'form': form})


def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')


