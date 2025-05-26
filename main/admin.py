from django.contrib import admin
from main.models import News, Images

# admin.site.register(News)
# admin.site.register(Images)

class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]