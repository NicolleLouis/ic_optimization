import json

import requests


class ImportDataService:
    base_url = "https://ps6.idlechampions.com/~idledragons/post.php?"

    game_data_relative_path = "call=getDefinitions"
    game_data_file = 'data_import/files/game_data.json'

    user_data_url = "call=getuserdetails"
    user_data_file = 'data_import/files/user_data.json'

    user_id = "90886"
    user_hash = "563f78772717e217e9e27381199e5ca1"

    @classmethod
    def import_game_data(cls):
        url = f"{cls.base_url}{cls.game_data_relative_path}"
        game_data = requests.get(
            url=url,
        ).json()

        file = open(cls.game_data_file, "w")
        json.dump(game_data, file, indent=6)
        file.close()

    @classmethod
    def import_user_data(cls):
        url = f"{cls.base_url}{cls.user_data_url}"
        params = {
            "instance_key": '1',
            "user_id": cls.user_id,
            "hash": cls.user_hash,
        }
        user_data = requests.get(
            url=url,
            params=params,
        ).json()

        file = open(cls.user_data_file, "w")
        json.dump(user_data, file, indent=6)
        file.close()
