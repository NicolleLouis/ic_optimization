from data_import.models import Hero
from data_import.models.meta_data import MetaDataRepository


class UpdateData:
    @staticmethod
    def update_hero_data():
        heroes = Hero.objects.all()
        list(
            map(
                lambda hero: hero.update_values(),
                heroes
            )
        )

    @staticmethod
    def update_metadata():
        MetaDataRepository.get_data().update()
