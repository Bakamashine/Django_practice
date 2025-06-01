from django.contrib import admin
from news.models import News
from django_summernote.admin import SummernoteModelAdmin

# class NewsImageInline(admin.TabularInline):
#     model = Images
#     extra = 1

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     inlines = [NewsImageInline]



@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
