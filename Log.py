import datetime


class Log:
    def __init__(self, buffered=False):
        self.__logs = []
        self.__buffered = buffered

    def log(self, line):
        log_line = "[{}] {}".format(datetime.datetime.now(), line)
        self.__logs.append(log_line) if self.__buffered else print(log_line)

    def error(self, line):
        self.log('>> {}'.format(line))

    def get_complete_log(self):
        return self.__logs;

if __name__ == '__main__':
    unbuf_log = Log()
    unbuf_log.log("this is a test log")

    buf_log = Log(True)
    buf_log.log("this is another test log")
    print(buf_log.get_complete_log())