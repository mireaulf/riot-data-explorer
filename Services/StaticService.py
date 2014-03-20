from Riot.Constants import Constants
from Riot.Services.RiotService import RiotService
from Riot.Model.Champion import Champion


class StaticService(RiotService):
    KEY_CHAMPION_DATA = 'data'

    def __init__(self):
        super().__init__()
        self.__champs = None
        self._base_url = Constants.URL_BASE_STATIC + '/' + self._region + "/{}?api_key=" + self.get_key()

    def __get_url_champions(self):
        return self._get_url(Constants.URL_CHAMPIONS)

    def __query_get_champions(self):
        return self._exec_request_json(self.__get_url_champions, None)

    def get_champions(self):
        if None is self.__champs:
            champs = self.__query_get_champions()[StaticService.KEY_CHAMPION_DATA]
            self.__champs = [Champion(champs[name]) for name in champs]
        return self.__champs

if '__main__' == __name__:
    static = StaticService()
    champs = static.get_champions()
    print(champs)
