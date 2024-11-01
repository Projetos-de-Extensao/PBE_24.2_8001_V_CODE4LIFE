from django.contrib import admin 
from .models import Content 
from .models import Usuario 

admin.site.register(Usuario) 
admin.site.register(Content)