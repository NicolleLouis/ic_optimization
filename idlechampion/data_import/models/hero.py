from django.contrib import admin
from django.db import models


class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    game_id = models.IntegerField()
    seat_id = models.IntegerField(
        null=True
    )
    name = models.CharField(
        max_length=30,
        null=True,
    )
    full_name = models.CharField(
        max_length=60,
        null=True,
    )
    alignment = models.CharField(
        max_length=60,
        null=True,
    )
    backstory = models.CharField(
        max_length=300,
        null=True,
    )
    hero_class = models.CharField(
        max_length=60,
        null=True,
    )
    race = models.CharField(
        max_length=60,
        null=True,
    )
    age = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    wisdom = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['game_id'], name='game_id'),
        ]


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


class HeroRepository:
    @staticmethod
    def get_or_create_by_game_id(game_id):
        return Hero.objects.get_or_create(game_id=game_id)
