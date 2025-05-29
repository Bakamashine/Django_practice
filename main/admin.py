from django.contrib import admin
from django.http import HttpRequest
from main.models import Feedback

# admin.site.register(Feedback)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False