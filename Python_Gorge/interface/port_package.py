"""
串口功能封装
"""
import serial
import serial.tools.list_ports
from log import logger

class Communication:

    def __init__(self, port, bps, timeout):
        self.port = port
        self.bps = bps
        self.timeout = timeout
        #定义一个标签
        global nbool

        #打开串口并得到串口对象
        try:
            self.ser = serial.Serial(self.port, self.bps, self.timeout)
            if self.ser.is_open:
                nbool = True
        except Exception as e:
            logger.error('打开串口并获取串口对象失败！')
            logger.error(e)


    #打印信息
    def print_name(self):
        print(self.ser.name)  # 设备名字
        print(self.ser.port)  # 读或者写端口
        print(self.ser.baudrate)  # 波特率
        print(self.ser.bytesize)  # 字节大小
        print(self.ser.parity)  # 校验位
        print(self.ser.stopbits)  # 停止位
        print(self.ser.timeout)  # 读超时设置
        print(self.ser.writeTimeout)  # 写超时
        print(self.ser.xonxoff)  # 软件流控
        print(self.ser.rtscts)  # 软件流控
        print(self.ser.dsrdtr)  # 硬件流控
        print(self.ser.interCharTimeout)  # 字符间隔超时


    #打开串口
    def open_gorge(self):
        self.ser.open()


    #关闭串口
    def close_gorge(self):
        self.ser.close()


    #定义一个装饰器
    @staticmethod
    def print_used_port():
        #获取可用串口
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print('无可用串口！')
        else:
            print(port_list)


if __name__ == '__main__':
    com = Communication('COM7', 9600, 6)
