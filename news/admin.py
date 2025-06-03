from django.contrib import admin
from news.models import News
from django_summernote.admin import SummernoteModelAdmin


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ["title", 'date']
    search_fields = ['title', 'date']
