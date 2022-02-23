import json

from data_import.models.hero import HeroRepository
from data_import.models.loot import LootRepository


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

    @classmethod
    def update_all_loot(cls):
        file = open(cls.game_data_file)
        loot_data = json.load(file)["details"]["loot"]
        for raw_loot in loot_data:
            cls.update_loot(raw_loot)
        file.close()

    @staticmethod
    def update_loot(raw_loot):
        slot_id = raw_loot["slot_id"]
        hero = HeroRepository.get_by_game_id(raw_loot['hero_id'])
        loot, _created = LootRepository.get_or_create(
            hero=hero,
            slot_id=slot_id,
        )
        loot.enchant = raw_loot['enchant']
        loot.gild = raw_loot['gild']
        loot.rarity = raw_loot['rarity']
        loot.save()

    @staticmethod
    def reset_all_heroes_unlock_state():
        HeroRepository.get_all().update(is_unlocked=False)

    @staticmethod
    def unlock_hero(raw_hero):
        game_id = raw_hero["hero_id"]
        hero = HeroRepository.get_by_game_id(game_id)
        hero.is_unlocked = True
        hero.save()