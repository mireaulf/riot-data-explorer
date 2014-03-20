from requests import get

from Riot.TestConstants import TestConstants
from Riot.Constants import Constants
from Riot.Log import Log


class RiotService:
    def __init__(self, key=TestConstants.API_KEY, region='na'):
        self.__log = Log()
        self.__key = key
        self._region = region
        self._base_url = Constants.URL_BASE + '/' + self._region + "/{}?api_key=" + key

    def get_key(self):
        return self.__key

    def _get_url(self, url):
        return self._base_url.format(url)

    def _exec_request_json(self, fn_get_url, args):
        url = fn_get_url() if None is args else fn_get_url(args)
        self.__log.log('Get request to {}'.format(url))
        response = get(url)
        self.__log.log('Get response: {}'.format(response))
        response_json = response.json()
        return response_json