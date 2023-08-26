from django.contrib import admin
from .models import Category, Tag, Author, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post)