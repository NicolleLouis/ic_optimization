from django.db import models
from django.contrib import admin

from data_import.models import Hero


class Loot(models.Model):
    id = models.AutoField(primary_key=True)
    slot_id = models.IntegerField(null=True)
    hero = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
    )
    enchant = models.IntegerField(
        null=True,
    )
    rarity = models.IntegerField(
        default=1,
    )
    gild = models.IntegerField(
        default=0,
    )

    class Meta:
        unique_together = [['hero', 'slot_id']]


@admin.register(Loot)
class LootAdmin(admin.ModelAdmin):
    list_display = (
        'hero',
        'slot_id',
    )

    search_fields = ('hero__name',)

    list_filter = (
        'rarity',
        'gild',
        'hero__availability',
    )

    def has_change_permission(self, request, obj=None):
        return False


class LootRepository:
    @staticmethod
    def get_or_create(hero, slot_id) -> (Loot, bool):
        return Loot.objects.get_or_create(
            hero=hero,
            slot_id=slot_id,
        )
