from django.contrib import admin
from news.models import News, Images

class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]
