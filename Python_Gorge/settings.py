##############串口界面设置信息 ################
#设置界面字体
FONT_AND_SIZE=('宋体', 16)
FONT_BUT_SIZE=('宋体', 14)

#设置串口号数组
GORGE_ARRAY = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7']
#设置默认串口
DEFAULT_GORGE = 'COM7'

#设置选择窗口大小
SELSIZE = (15, 9)

#设置波特率数组
BAUD_ARRAY = ['1200', '2400', '9600', '19200', '38400', '115200']
#设置波特率默认大小
DEFAULT_SIZE = '9600'

#设置数据位列表
DATA_BIT = ['5', '6', '7', '8']
#设置数据位默认大小
DEFAULT_DATA_BIT = '8'

#设置停止位列表
STOP_BIT = ['1', '1.5', '2']
#设置停止位默认大小
DEFAULT_STOP_BIT = '1'

#设置发送数据的写入窗口大小
SEND_DATA_SIZE=(16, 8)

#设置右侧Frame框架大小
FRAME_SIZE=(50, 6)

##############日志信息################
import logging
#设置默认等级
LOG_LEVEL = logging.DEBUG
#filename:指输出日志的文件名称
LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(name)s: %(message)s'
#默认时间格式
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
#日志文件名称
LOG_FILENAME = 'log.log'