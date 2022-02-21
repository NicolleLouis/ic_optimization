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
        'seat_id',
        'race',
        'alignment',
        'hero_class',
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
    )

    inlines = [
        TagInLine,
    ]

    list_filter = (
        'availability',
    )
