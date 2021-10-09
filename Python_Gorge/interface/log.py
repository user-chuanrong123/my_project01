"""
日志文件--GUI界面
"""

import logging

class MyLog:
    #执行日志函数
    def do_log(self, msg, level):
        #创建一个容器，存放日志
        my_log = logging.getLogger('GUI调试')
        #设定等级
        my_log.setLevel('REEOR')
        #定义输出格式
        myFormatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s: %(message)s')
        #创建输出渠道
        ch = logging.StreamHandler() #输出到控制台
        ch.setLevel('DEBUG')
        ch.setFormatter(myFormatter) #设置输出格式
        fh = logging.FileHandler(r'E:\SOFT_GX96\text_log.txt', encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(myFormatter)  # 设置输出格式
        #指定我们容器中日志的输出渠道
        my_log.addHandler(ch)
        my_log.addHandler(fh)


        if level == 'DEBUG':
            my_log.debug(msg)
        if level == 'INFO':
            my_log.info(msg)
        if level == 'ERROR':
            my_log.error(msg)
        if level == 'WARNING':
            my_log.warning(msg)
        if level == 'CRITICAL':
            my_log.critical(msg)

        #关闭渠道
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)


if __name__ == '__main__':
    MyLog().do_log('加油', 'ERROR')








