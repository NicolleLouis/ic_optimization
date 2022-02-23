import json

from data_import.models.hero import HeroRepository


class ConvertUserData:
    game_data_file = 'data_import/files/user_data.json'

    @classmethod
    def unlock_heroes(cls):
        cls.reset_all_heroes_unlock_state()
        file = open(cls.game_data_file)
        heroes_data = json.load(file)["details"]["heroes"]
        for raw_hero in heroes_data:
            cls.unlock_hero(raw_hero)
        file.close()

    @staticmethod
    def reset_all_heroes_unlock_state():
        HeroRepository.get_all().update(is_unlocked=False)

    @staticmethod
    def unlock_hero(raw_hero):
        game_id = raw_hero["hero_id"]
        hero = HeroRepository.get_by_game_id(game_id)
        hero.is_unlocked = True
        hero.save()