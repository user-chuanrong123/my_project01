"""
串口调试界面
"""
import datetime
import time

import PySimpleGUI as sg
from log import logger
from settings import *
from port_package import Communication
from  yaml_demo import file, data
from threading import Thread
import _thread
import serial.tools.list_ports

# 实例化通信类
com = Communication('/dev/ttyUSB0', 9600)

GORGE_ARRAY = []
for item in com.print_used_port():
    GORGE_ARRAY.append(str(item))
print(GORGE_ARRAY)


#主题
sg.theme('Default1')



# 左侧框架设计
frame_layout1 = [
    [sg.Text('串口号:', font=FONT_AND_SIZE),
     sg.Combo(GORGE_ARRAY, font=FONT_BUT_SIZE, key='-GORGE_NUMBER-',  size=SELSIZE, default_value=GORGE_ARRAY[0])],
    [sg.Text('波特率:', font=FONT_AND_SIZE),
     sg.Combo(BAUD_ARRAY, font=FONT_BUT_SIZE, key='-BAUD_NUMBER-', default_value=DEFAULT_SIZE, size=SELSIZE)],
    [sg.Text('校验位:', font=FONT_AND_SIZE),
     sg.Combo(CHECKOUT_LIST, font=FONT_BUT_SIZE, key='-PARITY_BIT-', default_value=DEFAULE_CHECKOUT, size=SELSIZE)],
    [sg.Text('数据位:', font=FONT_AND_SIZE),
     sg.Combo(DATA_BIT, font=FONT_BUT_SIZE, key='-DATA_BIT-', default_value=DEFAULT_DATA_BIT, size=SELSIZE)],
    [sg.Text('停止位:', font=FONT_AND_SIZE),
     sg.Combo(STOP_BIT, font=FONT_BUT_SIZE, key='-STOP_BIT-', default_value=DEFAULT_STOP_BIT, size=SELSIZE)],
    [sg.Button('打开串口', font=FONT_BUT_SIZE, key='-OPEN_BUTTEN-'),
     sg.Button('关闭串口', font=FONT_BUT_SIZE, key='-CLOSE_BUTTEN-')],
    # [sg.Text('')],
    [sg.Radio('ASCII', 'R1', key='-ASCII-',font=FONT_BUT_SIZE, size=(7,10), default=True), sg.Radio('Hex', 'R1', key='-HEX-', font=FONT_BUT_SIZE, size=(7,10))],
    [sg.Button('发送', font=FONT_BUT_SIZE, key='-SEND_DATA-'),
     sg.Combo(SEND_LIST, font=FONT_BUT_SIZE, key='-SEND_CONTENT-', default_value=DEFAULE_SEND, size=SELSIZE)],
    [sg.Button('接收', font=FONT_BUT_SIZE, key='-RECIPT_DATA-')]
]

# 右侧框架设计
frame_layout2 = [
    [sg.Text('发送数据:', font=FONT_BUT_SIZE), sg.Button('清除发送数据', font=FONT_BUT_SIZE, key='-CLEAR_SENDDATA-')],
    [sg.Listbox('', size=FRAME_SIZE, key='-PB2-')],
    [sg.Text('接收数据:', font=FONT_BUT_SIZE), sg.Button('清除接收数据', font=FONT_BUT_SIZE, key='-CLEAR_RECIPT-')],
    [sg.Listbox('', size=FRAME_SIZE, key='-PB3-')]
]

# 整体布局
Layout = [
    [sg.Frame('', frame_layout1), sg.Frame('', frame_layout2)]
]

window = sg.Window('串口调试工具', Layout)



while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        # 退出
        break

    if event == '-OPEN_BUTTEN-':
        # 打开串口
        if com.flag == 1:
            print('串口已经处于启动状态')
            window['-PB2-'].update(['提示：当前串口状态>>>开启'])
        else:
            com.open_gorge()
            if com.ser.is_open:
                com.flag = 1
                print('init ---succfy')
                window['-PB2-'].update(['提示：当前串口状态>>>开启'])
            else:
                print('open gorge fail')
                com.flag = 0





    if event == '-CLOSE_BUTTEN-':
        # 关闭串口
        com.close_gorge()
        if not com.ser.is_open:
            print('关闭串口成功')
            com.flag = 0
            window['-PB2-'].update(['提示：关闭串口成功'])
        else:
            print('关闭串口失败')
            com.flag = 1
            window['-PB2-'].update(['提示：关闭串口失败'])



    if event == '-SEND_DATA-':
        # 发送数据
        if com.flag == 1:
            templist = []
            if values['-SEND_CONTENT-'] == "data['content1']":
                result = com.send_messages(data['content1'])
                templist.append(data['content1'])
            elif values['-SEND_CONTENT-'] == "data['content2']":
                result = com.send_messages(data['content2'])
                templist.append(data['content2'])

            window['-PB2-'].update(templist)
            if values['-HEX-'] == True:
                rData = com.reception_messages_size()
                window['-PB3-'].update([rData])

            else:
                window['-PB3-'].update(templist)
        else:
            window['-PB2-'].update(['提示：当前串口处于关闭状态，请打开串口后在发送信息！'])

    if event == '-RECIPT_DATA-':
        #接收数据
        if com.flag == 1:
            print("开始接收数据：")
            window['-PB3-'].update(['暂不支持手动接收数据'])
        else:
            window['-PB3-'].update(['提示：当前串口处于关闭状态，无法接受消息！'])



    if event == '-CLEAR_SENDDATA-':
        window['-PB2-'].update([])

    if event == '-CLEAR_RECIPT-':
        window['-PB3-'].update([])
    print(event)
    print(values)

window.close()
