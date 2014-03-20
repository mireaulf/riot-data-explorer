class Summoner:
    def __init__(self, kvpair):
        self.__name = kvpair.get('name')
        self.__id = kvpair.get('id')
        self.__level = kvpair.get('summonerLevel')
        self.__games = []

    def __str__(self):
        return "{}({}) is level {}".format(self.__name, self.__id, self.__level)

    def __repr__(self):
        return self.__str__()

    def get_id(self):
        return self.__id