from logging.handlers import RotatingFileHandler
import logging
from common.handlepath import loglog


class Logger:

    def __init__(self):

        # 创建一个日志接收器
        self.case_logger = logging.getLogger('case')
        # 定义日志接收等级
        self.case_logger.setLevel('INFO')
        # 创建日志接收渠道
        self.console_handle = logging.StreamHandler()
        # 定义日志文件格式
        self.file_handle = RotatingFileHandler(filename=loglog,
                                               mode='a',
                                               maxBytes=1048576,
                                               backupCount=3,
                                               encoding='utf8')

        self.console_handle.setLevel('INFO')
        self.file_handle.setLevel('INFO')


        fmt = "%(asctime)s- [%(levelname)s] - %(module)s - %(threadName)s- %(name)s- %(lineno)d - [日志信息]:%(message)s"
        self.handle_formatter = logging.Formatter(fmt)
        self.console_handle.setFormatter(self.handle_formatter)
        self.file_handle.setFormatter(self.handle_formatter)

        self.case_logger.addHandler(self.console_handle)
        self.case_logger.addHandler(self.file_handle)


    def get_logger(self):
        return self.case_logger


logger = Logger().get_logger()


if __name__ == '__main__':
    logger.info('aaaa')