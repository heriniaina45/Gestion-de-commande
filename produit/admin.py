from django.contrib import admin
from .models import Produit
from .models import Tag

admin.site.register(Produit)
admin.site.register(Tag)