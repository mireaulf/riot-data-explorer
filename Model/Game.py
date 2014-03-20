from Riot.Model.GameStats import GameStats
from Riot.Constants import Constants


class Game:
    def __init__(self, kv_game):
        self.__mode = kv_game['gameMode']
        self.__type = kv_game['gameType']
        self.__sub_type = kv_game['subType']
        self.__champion_id = kv_game['championId']
        self.__stats = GameStats(kv_game.get('stats', None))

    def __str__(self):
        return "{} - {} - {} -> {}".format(self.__sub_type, self.__mode, self.__type, self.__stats)

    def __repr__(self):
        return self.__str__()

    def is_ranked_solo(self):
        return self.__sub_type == Constants.RANKED_SOLO_5_STRING

    def is_ranked_team_5(self):
        return self.__sub_type == Constants.RANKED_TEAM_5_STRING

    def get_champion_id(self):
        return self.__champion_id
