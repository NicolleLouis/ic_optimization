from django.db import models
from django.contrib import admin

from data_import.models import Hero
from data_import.models.hero import HeroRepository


class MetaData(models.Model):
    id = models.AutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    average_ilvl = models.IntegerField(
        null=True,
    )
    lowest_ilvl = models.IntegerField(
        null=True,
    )
    lowest_hero = models.ForeignKey(
        Hero,
        on_delete=models.SET_NULL,
        null=True,
    )

    def update(self):
        heroes = HeroRepository.get_all()
        all_ilvl = []

        for hero in heroes:
            if hero.is_unlocked and hero.average_loot_level is not None:
                hero.update_values()
                all_ilvl.append(hero.average_loot_level)

        self.lowest_ilvl = min(all_ilvl)
        self.average_ilvl = sum(all_ilvl) / len(all_ilvl)

        for hero in heroes:
            if hero.is_unlocked:
                if hero.average_loot_level == self.lowest_ilvl:
                    self.lowest_hero = hero

        self.save()


@admin.register(MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    list_display = (
        "average_ilvl",
        "lowest_ilvl",
        "lowest_hero",
    )

    def has_change_permission(self, request, obj=None):
        return False


class MetaDataRepository:
    @staticmethod
    def get_data() -> MetaData:
        return MetaData.objects.all()[0]
