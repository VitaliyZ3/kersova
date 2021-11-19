from django.contrib import admin
from .models import Abonement, Trainer

# Register your models here.

admin.site.register(Abonement)
admin.site.register(Trainer)

class MyAdmin(admin.ModelAdmin):
    def log_addition(self, *args):
            return
    def log_change(self, *args):
            return
    def log_deletion(self, *args):
            return