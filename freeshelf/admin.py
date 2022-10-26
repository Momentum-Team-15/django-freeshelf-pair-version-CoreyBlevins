from django.contrib import admin
from .models import User, Resource, Category, Favorite


admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Category)
admin.site.register(Favorite)
