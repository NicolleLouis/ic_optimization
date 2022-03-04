from django.db import models

from data_import.constants.hero_availability import HeroAvailability


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
    availability = models.CharField(
        max_length=12,
        choices=HeroAvailability.HeroAvailabilityChoice,
        default=HeroAvailability.EVENT,
        blank=False,
    )
    should_pay_tribute = models.BooleanField(
        default=False,
        verbose_name='GOAT',
    )
    is_unlocked = models.BooleanField(
        default=False,
    )
    average_loot_level = models.IntegerField(
        null=True,
    )

    def __str__(self):
        return self.name

    def update_values(self):
        self.compute_average_loot_level()
        self.save()

    def compute_average_loot_level(self):
        loots = self.loots.all()
        if len(loots) == 0:
            return None
        loots_level = list(
            map(
                lambda loot: loot.enchant,
                loots
            )
        )
        average_loot_level = int(
            sum(loots_level)/len(loots_level)
        )
        self.average_loot_level = average_loot_level

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['game_id'], name='game_id'),
        ]


class HeroRepository:
    @staticmethod
    def get_all() -> models.query.QuerySet:
        return Hero.objects.all()

    @staticmethod
    def get_or_create_by_game_id(game_id) -> (Hero, bool):
        return Hero.objects.get_or_create(game_id=game_id)

    @staticmethod
    def get_by_game_id(game_id) -> Hero:
        return Hero.objects.get(game_id=game_id)

    @staticmethod
    def get_number_of_tribute_champion() -> int:
        return Hero.objects.filter(should_pay_tribute=True).count()

    @staticmethod
    def get_tribute_champion() -> models.query.QuerySet:
        return Hero.objects.filter(should_pay_tribute=True)
