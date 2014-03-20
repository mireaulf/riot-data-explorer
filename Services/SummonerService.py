from Riot.Services.RiotService import RiotService
from Riot.Model.Summoner import Summoner
from Riot.TestConstants import TestConstants


class SummonerService(RiotService):
    def __init__(self):
        super().__init__()

    def __get_url_summoners(self, name_list):
        if not isinstance(name_list, list):
            raise TypeError('Expected a list of string')
        names = ','.join(name for name in name_list)
        url = self._get_url("v1.3/summoner/by-name/{}".format(names))
        return url

    def get_summoners(self, name_list):
        summoner_list = []
        if isinstance(name_list, list):
            low_case_name_list = [name.lower() for name in name_list]
            response_json = self._exec_request_json(self.__get_url_summoners, low_case_name_list)
            summoner_list = [Summoner(response_json[name]) for name in low_case_name_list]
        else:
            self.__log.error('Expected a list')
        return summoner_list

    def get_summoner(self, name):
        lower_case_name = name.lower()
        return self.get_summoners([lower_case_name])[0]

if __name__ == '__main__':
    sumService = SummonerService()
    summs = sumService.get_summoners([TestConstants.DEFAULT_SUMMONER_NAME])
    print(summs)


