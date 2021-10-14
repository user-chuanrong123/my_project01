"""
串口功能封装
"""
import serial
# import serial.tools.list_ports
from log import logger
import serial.tools.list_ports

class Communication:
    """通信类"""

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
                logger.info('成功打开串口并创建对象！')
        except Exception as e:
            logger.error('打开串口并获取串口对象失败！')
            logger.error(e)



    def print_name(self):
        """打印信息"""
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



    def open_gorge(self):
        """打开串口"""
        self.ser.open()


    def close_gorge(self):
        """关闭串口"""
        self.ser.close()


    # @staticmethod
    def print_used_port(self):
        """获取可用串口"""
        port_list = list(serial.tools.list_ports.comports())
        if port_list:
            for i in range(len(port_list)):
                print(port_list[i])
        else:
            logger.info('没有搜索到任何可用的串口！')





    def send_messages(self, data):
        """发送数据"""
        return self.ser.write(data.encode('UTF-8'))


    def reception_messages_size(self, size):
        """功能函数：接收指定字节大小得数据"""
        return  self.ser.read(size=size)


    def reception_messages_line(self):
        """功能函数：接收一行数据"""
        return self.ser.readline()

    def reception_messages_all(self):
        """功能函数：从端口接收所有数据"""
        return self.ser.read_all()





if __name__ == '__main__':
    com = Communication('COM1', 9600, 5)
    com.print_used_port()

