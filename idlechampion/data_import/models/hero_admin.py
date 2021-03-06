from django.contrib import admin

from data_import.models.hero import Hero
from data_import.models import Tag


class TagInLine(admin.TabularInline):
    model = Tag
    readonly_fields = ("label",)
    can_delete = False

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'average_loot_level',
        'race',
        'alignment',
        'hero_class',
        'should_pay_tribute',
        'is_unlocked',
    )

    readonly_fields = (
        'name',
        'seat_id',
        'race',
        'alignment',
        'hero_class',
        'full_name',
        'alignment',
        'backstory',
        'age',
        'charisma',
        'constitution',
        'dexterity',
        'intelligence',
        'strength',
        'wisdom',
        'game_id',
        'average_loot_level',
        'is_unlocked',
    )

    inlines = [
        TagInLine,
    ]

    list_filter = (
        'availability',
        'seat_id',
        'is_unlocked',
    )

    search_fields = (
        'name',
    )
