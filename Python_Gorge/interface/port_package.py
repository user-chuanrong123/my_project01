import sys

import serial
import serial.tools.list_ports

from _thread import start_new_thread


class Communication:
    def __init__(self, port, bps):
        self.port = port
        self.bps = bps
        # self.port_list = []
        self.flag = 1
        self.nData1 = ''

        try:
            self.ser = serial.Serial(self.port, self.bps)
            if self.ser.is_open:
                print('init ---succeed')
        except Exception as e:
            print('init ---fail')
            print(e)

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
        return self.ser.open()


    def close_gorge(self):
        """关闭串口"""
        print('closing...')
        return self.ser.close()


    def print_used_port(self):
        """获取可用串口"""
        port_list = list(serial.tools.list_ports.comports())

        return port_list

    def send_messages(self, data):
        """发送数据"""
        f_number = self.ser.write(data.encode('UTF-8'))
        return f_number

    def thread_fun1(self):

        while True:
            if self.ser.in_waiting:
                for i in range(self.ser.in_waiting):
                    item = self.ser.read(1).hex()
                    self.nData1 += ''.join(item)
                    nData2 = int(self.nData1, 16)
                    if nData2 == 'exit':
                        break

    def thread_fun2(self):

        return self.nData1


    def reception_messages_size(self):
        """功能函数：接收数据"""
        t1 = start_new_thread(self.thread_fun1, ())
        t2 = start_new_thread(self.thread_fun2, ())

        return self.thread_fun2()





if __name__ == '__main__':
    com = Communication('/dev/ttyUSB0', 9600)
    com.print_used_port()
