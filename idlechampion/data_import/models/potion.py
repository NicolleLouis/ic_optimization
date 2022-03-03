from django.db import models
from django.contrib import admin


class Potion(models.Model):
    id = models.AutoField(primary_key=True)
    potion_id = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    name = models.CharField(
        max_length=60,
        null=True,
    )

    def __str__(self):
        return f'{self.potion_id}: {self.amount}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['potion_id'], name='potion_id'),
        ]


@admin.register(Potion)
class PotionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
    )

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return Potion.objects.filter(amount__gt=0)

    ordering = ['-amount']


class PotionRepository:
    @staticmethod
    def get_or_create(potion_id) -> (Potion, bool):
        return Potion.objects.get_or_create(
            potion_id=potion_id,
        )
