from django.contrib import admin
from django.db import models

from data_import.models.hero import Hero


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=30)
    hero = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        null=True,
        related_name="tags",
    )

    def __str__(self):
        return self.label

    class Meta:
        unique_together = [['hero', 'label']]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('label', 'hero')

    list_filter = ('hero',)


class TagRepository:
    @staticmethod
    def get_by_label(label):
        return Tag.objects.filter(label=label)
