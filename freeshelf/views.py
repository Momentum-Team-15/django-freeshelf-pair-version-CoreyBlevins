from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource, Category, Favorite
from freeshelf.forms import ResourceForm


@login_required
def index(request):
    resources = Resource.objects.all().order_by('-created_date')
    categories = Category.objects.all()
    starred = Favorite.objects.all()
    return render(request, 'freeshelf/index.html', {'resources': resources, 'categories': categories, 'starred': starred})


def add_favorite(request, res_pk):
    resource = get_object_or_404(Resource, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(resource=resource, user=request.user)
        favorite.save()
    return redirect("home")


def favorite(request):
    favorited = Favorite.objects.all().order_by('-created_at')
    return render(request, 'freeshelf/favorites.html', {'favorited': favorited})


def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'freeshelf/resource_detail.html', {'resource': resource})


def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'freeshelf/resource_categories.html', {'category': category})


def edit_resources(request, pk):
    edit = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('resource_detail', pk=edit.pk)
    else:
        form = ResourceForm(instance=edit)
    return render(request, 'freeshelf/edit_resource.html', {'form': form})


def delete_resource(request, pk):
    edit = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        edit.delete()
        return redirect("home")
    return render(request, 'freeshelf/delete_resource.html')


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


def image_upload(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ResourceForm()
    return render(request, 'index.html', {'form': form})