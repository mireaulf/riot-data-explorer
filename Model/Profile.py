from os.path import expanduser, isfile
import shelve
from contextlib import closing

from Riot.TestConstants import TestConstants
from Riot.Log import Log
from Riot.Services.StaticService import StaticService


class Profile:

    class Constants:
        KEY_CHAMPIONS = 'champs'
        KEY_SUMMONERS_NAME = 'summs_name'

        DEFAULT_CHAMPIONS = None
        DEFAULT_SUMMONERS_NAME = list()

    def __init__(self, name):
        self.__log = Log()
        self.__serviceStatic = StaticService()
        self.__path = expanduser('~/{}'.format(name))
        self.__champs = Profile.Constants.DEFAULT_CHAMPIONS
        self.__summs_name = Profile.Constants.DEFAULT_SUMMONERS_NAME

    def load(self):
        if isfile(self.__path):
            with closing(shelve.open(self.__path, 'w')) as kvstore:
                self.__champs = kvstore.get(Profile.Constants.KEY_CHAMPIONS,
                                            Profile.Constants.DEFAULT_CHAMPIONS)
                self.__summs_name = kvstore.get(Profile.Constants.KEY_SUMMONERS_NAME,
                                                Profile.Constants.DEFAULT_SUMMONERS_NAME)
            self.__log.log('Profile loaded from "{}"'.format(self.__path))
        else:
            self.__log.log('File not found("{}"): new profile'.format(self.__path))

    def save(self):
        open_mode = 'w' if isfile(self.__path) else 'c'
        with closing(shelve.open(self.__path, open_mode)) as kvstore:
            kvstore[Profile.Constants.KEY_CHAMPIONS] = self.__champs
            kvstore[Profile.Constants.KEY_SUMMONERS_NAME] = self.__summs_name
        self.__log.log('Profile saved to "{}"'.format(self.__path))

    def get_champions(self):
        if None == self.__champs:
            self.__champs = self.__serviceStatic.get_champions()
        return self.__champs

    def register_summoner_name(self, summ_name):
        if isinstance(summ_name, str):
            self.__summs_name.append(summ_name.strip().lower())
        else:
            self.__log.error('Expected a summoner name')


if __name__ == '__main__':
    acc = Profile(TestConstants.DEFAULT_PROFILE_NAME)
    acc.load()
    print(acc.get_champions())
    acc.register_summoner_name(TestConstants.DEFAULT_SUMMONER)
    acc.save()

