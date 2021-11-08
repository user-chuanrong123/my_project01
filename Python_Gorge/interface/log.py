"""
日志
日志的级别排序: CRITICAL > ERROR > WARNING > INFO > DEBUG
"""

import logging
import sys
from Python_Gorge import settings


class Logger(object):

    def __init__(self):
        #1:获取一个logger对象
        self._logger = logging.getLogger()
        #定义日志输出格式
        self.formatter = logging.Formatter(fmt=settings.LOG_FMT, datefmt=settings.LOG_DATEFMT)
        #指定日志输出渠道
        self._logger.addHandler(self._get_file_handler(settings.LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        #设置日志文件的等级
        self._logger.setLevel(settings.LOG_LEVEL)


    def _get_file_handler(self, filename):
        """返回一个文件日志handler"""
        #1:获取一个文件日志handler
        filehandler = logging.FileHandler(filename=filename, encoding='utf-8')
        #2:设置日志格式
        filehandler.setFormatter(self.formatter)
        #3:返回
        return filehandler


    def _get_console_handler(self):
        """返回一个输出到终端日志handler"""
        #1:获取一个输出到终端的handler
        console_handler = logging.StreamHandler(sys.stdout)
        #2:设置日志格式
        console_handler.setFormatter(self.formatter)
        #3:返回handler
        return console_handler


    @property # https://zhuanlan.zhihu.com/p/64487092
    def logger(self):
        return self._logger


#初始化并配一个logger对象
#使用时，直接导入logger就可用使用settings.py

logger = Logger().logger

if __name__ == '__main__':
    logger.debug('11')
    logger.info('22')
    logger.warning('33')
    logger.error('44')