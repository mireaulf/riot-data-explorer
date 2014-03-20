class GameStats:
    def __init__(self, kv_stats):
        self.__win = kv_stats.get('win')
        self.__gold_spent = kv_stats.get('goldSpent', 0)
        self.__gold_earned = kv_stats.get('goldEarned', 0)
        self.__kill_champs = kv_stats.get('championsKilled', 0)
        self.__kill_minions = kv_stats.get('minionsKilled', 0)
        self.__kill_nexus = kv_stats.get('nexusKilled', False)
        self.__assists = kv_stats.get('assists', 0)
        self.__deaths = kv_stats.get('numDeaths', 0)
        self.__wards_placed = kv_stats.get('wardPlaced', 0)

    def get_kill_champs(self):
        return self.__kill_champs

    def get_kill_minions(self):
        return self.__kill_minions

    def get_assists(self):
        return self.__assists

    def get_deaths(self):
        return self.__deaths

    def is_won(self):
        return self.__win

    def get_kda(self):
        deaths = self.get_deaths()
        if 0 == deaths:
            deaths = 1
        return (self.get_kill_champs() + self.get_assists()) / deaths

    def __str__(self):
        return "Win({}): {:2}/{:2}/{:2}".format(str(1 if self.is_won() else 0),
                                                    self.get_kill_champs(),
                                                    self.get_deaths(),
                                                    self.get_assists())

    def __repr__(self):
        return self.__str__()