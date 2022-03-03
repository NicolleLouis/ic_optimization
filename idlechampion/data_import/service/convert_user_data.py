import json

from data_import.models.hero import HeroRepository
from data_import.models.loot import LootRepository
from data_import.models.potion import PotionRepository


class ConvertUserData:
    game_data_file = 'data_import/files/user_data.json'

    @classmethod
    def unlock_heroes(cls):
        cls.reset_all_heroes_unlock_state()
        file = open(cls.game_data_file)
        file.close()
        heroes_data = json.load(file)["details"]["heroes"]
        for raw_hero in heroes_data:
            cls.unlock_hero(raw_hero)

    @classmethod
    def update_all_loot(cls):
        file = open(cls.game_data_file)
        loot_data = json.load(file)["details"]["loot"]
        file.close()
        for raw_loot in loot_data:
            cls.update_loot(raw_loot)

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

    @classmethod
    def update_all_potion(cls):
        file = open(cls.game_data_file)
        potion_data = json.load(file)["details"]["buffs"]
        file.close()
        for raw_potion in potion_data:
            cls.update_potion(raw_potion)

    @staticmethod
    def update_potion(raw_potion):
        potion_id = raw_potion["buff_id"]
        potion, _created = PotionRepository.get_or_create(
            potion_id=potion_id,
        )
        potion.amount = raw_potion['inventory_amount']
        potion.save()

    @staticmethod
    def reset_all_heroes_unlock_state():
        HeroRepository.get_all().update(is_unlocked=False)

    @staticmethod
    def unlock_hero(raw_hero):
        game_id = raw_hero["hero_id"]
        hero = HeroRepository.get_by_game_id(game_id)
        hero.is_unlocked = True
        hero.save()
