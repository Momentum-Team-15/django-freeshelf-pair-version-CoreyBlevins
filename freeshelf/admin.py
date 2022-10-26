from django.contrib import admin
from .models import User, Resource, Category


admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Category)
