import json

import django

from data_import.models import Tag
from data_import.models.hero import HeroRepository
from data_import.models.potion import PotionRepository


class ConvertGameData:
    game_data_file = 'data_import/files/game_data.json'

    @classmethod
    def generate_potions_from_game_data(cls):
        file = open(cls.game_data_file)
        all_potion_data = json.load(file)["buff_defines"]
        file.close()
        for raw_potion_data in all_potion_data:
            cls.convert_raw_potion_data(raw_potion_data)

    @staticmethod
    def convert_raw_potion_data(raw_potion_data):
        potion_id = raw_potion_data["id"]
        potion, _created = PotionRepository.get_or_create(
            potion_id=potion_id
        )
        potion.name = raw_potion_data["name"]
        potion.save()

    @classmethod
    def generate_heroes_from_game_data(cls):
        file = open(cls.game_data_file)
        heroes_data = json.load(file)["hero_defines"]
        file.close()
        for hero_data in heroes_data:
            cls.convert_raw_hero_data(hero_data)

    @staticmethod
    def convert_raw_hero_data(raw_hero_data):
        game_id = raw_hero_data["id"]
        hero, _created = HeroRepository.get_or_create_by_game_id(
            game_id=game_id
        )
        character_sheet_details = raw_hero_data["character_sheet_details"]
        ability_scores = character_sheet_details["ability_scores"]

        hero.name = raw_hero_data["name"]

        print(raw_hero_data["name"])

        hero.backstory = character_sheet_details["backstory"]
        hero.hero_class = character_sheet_details["class"]
        hero.seat_id = raw_hero_data["seat_id"]
        hero.race = character_sheet_details["race"]
        hero.full_name = character_sheet_details["full_name"]
        hero.save()

        try:
            hero.alignment = character_sheet_details["alignment"]
            hero.age = character_sheet_details["age"]
            hero.charisma = ability_scores["cha"]
            hero.constitution = ability_scores["con"]
            hero.dexterity = ability_scores["dex"]
            hero.intelligence = ability_scores["int"]
            hero.strength = ability_scores["str"]
            hero.wisdom = ability_scores["wis"]

            hero.save()
        except Exception as e:
            print(e)

        raw_tags = raw_hero_data["tags"]
        for raw_tag in raw_tags:
            tag = Tag(
                label=raw_tag,
                hero=hero
            )
            try:
                tag.save()
            except django.db.utils.IntegrityError:
                pass
