"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from freeshelf import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name="home"),
    path('accounts/logout/', views.logout, name="logout"),
    path('accounts/login/', views.login, name="login"),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resource/<int:pk>/edit', views.edit_resources, name='edit_resource'),
    path('resource/new', views.create_resource, name='create_resource'),
    path('resource/<int:pk>/delete', views.delete_resource, name='delete_resource'),
    path('resource/<slug:slug>/', views.category, name='resource_categories'),
    path('favorites/new/<int:res_pk>', views.add_favorite, name='favorite'),
    path('favorites/', views.favorite, name='favorite_page'),
    path('upload/', views.image_upload, name='image_uplaod')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)