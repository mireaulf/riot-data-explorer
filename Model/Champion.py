class Champion:
    def __init__(self, kv_champ):
        self.__name = kv_champ['name']
        self.__key = kv_champ['key']

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__str__()

    def get_key(self):
        return self.__key

    def get_name(self):
        return self.__name