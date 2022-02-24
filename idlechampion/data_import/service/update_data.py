from data_import.models import Hero


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
