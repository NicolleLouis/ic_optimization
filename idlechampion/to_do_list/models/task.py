from django.contrib import admin
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(done=False)
