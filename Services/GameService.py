from Riot.TestConstants import TestConstants
from Riot.Services.RiotService import RiotService
from Riot.Model.Game import Game


class GameService(RiotService):
    KEY_GAMES = 'games'

    def __init__(self):
        super().__init__()

    def __get_url_games_recent(self, summoner_id):
        return self._get_url('v1.3/game/by-summoner/{summonerId}/recent'.format(summonerId=summoner_id))

    def get_games_recent(self, summoner_id):
        json_response = self._exec_request_json(self.__get_url_games_recent, summoner_id)
        json_games = json_response[GameService.KEY_GAMES]
        return [Game(json_game) for json_game in json_games]

if '__main__' == __name__:
    gameService = GameService()
    games = gameService.get_games_recent(TestConstants.DEFAULT_SUMMONER)
    print(games)