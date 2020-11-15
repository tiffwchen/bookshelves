from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'summary', 'page_count')
    list_display= ('title', 'author', 'summary')

admin.site.register(Book, BookAdmin)