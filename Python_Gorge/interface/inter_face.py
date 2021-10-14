"""
串口调试界面
"""
import datetime
import time

import PySimpleGUI as sg
from log import logger
from settings import GORGE_ARRAY
from settings import DEFAULT_GORGE
from settings import SELSIZE
from settings import BAUD_ARRAY
from settings import DEFAULT_SIZE
from settings import FONT_AND_SIZE
from settings import FONT_BUT_SIZE
from settings import DATA_BIT
from settings import STOP_BIT
from settings import DEFAULT_DATA_BIT
from settings import DEFAULT_STOP_BIT
from settings import SEND_DATA_SIZE
from settings import FRAME_SIZE
from settings import CHECKOUT
from port_package import Communication

#左侧框架设计
frame_layout1 = [
	    [sg.Text('串口号:', font=FONT_AND_SIZE), sg.Combo(GORGE_ARRAY, font=FONT_BUT_SIZE, key='-GORGE_NUMBER-', default_value=DEFAULT_GORGE, size=SELSIZE)],
	    [sg.Text('波特率:', font=FONT_AND_SIZE), sg.Combo(BAUD_ARRAY, font=FONT_BUT_SIZE, key='-BAUD_NUMBER-', default_value=DEFAULT_SIZE, size=SELSIZE)],
	    [sg.Text('校验位:', font=FONT_AND_SIZE), sg.Combo(CHECKOUT, font=FONT_BUT_SIZE, key='-PARITY_BIT-', default_value=CHECKOUT, size=SELSIZE)],
	    [sg.Text('数据位:', font=FONT_AND_SIZE), sg.Combo(DATA_BIT, font=FONT_BUT_SIZE, key='-DATA_BIT-', default_value=DEFAULT_DATA_BIT, size=SELSIZE)],
	    [sg.Text('停止位:', font=FONT_AND_SIZE), sg.Combo(STOP_BIT, font=FONT_BUT_SIZE, key='-STOP_BIT-', default_value=DEFAULT_STOP_BIT, size=SELSIZE)],
	    [sg.Button('打开串口', font=FONT_BUT_SIZE, key='-OPEN_BUTTEN-'), sg.Button('关闭串口', font=FONT_BUT_SIZE, key='-CLOSE_BUTTEN-')],
	    [sg.Text('')],
	    [sg.Button('发送', font=FONT_BUT_SIZE, key='-SEND_DATA-'), sg.Input(size=SEND_DATA_SIZE, font=FONT_BUT_SIZE, key='-INPUT_TEXT-')],
	    [sg.Button('接收', font=FONT_BUT_SIZE, key='-RECIPT_DATA-')]
]

#右侧框架设计
frame_layout2 = [
	[sg.Text('发送数据:', font=FONT_BUT_SIZE), sg.Button('清除发送数据', font=FONT_BUT_SIZE, key='-CLEAR_SENDDATA-')],
	[sg.Listbox('', size=FRAME_SIZE, key='-PB2-')],
	[sg.Text('接收数据:', font=FONT_BUT_SIZE), sg.Button('清除接收数据', font=FONT_BUT_SIZE, key='-CLEAR_RECIPT-')],
	[sg.Listbox('', size=FRAME_SIZE, key='-PB3-')]
]

#整体布局
Layout = [
   	[sg.Frame('', frame_layout1),sg.Frame('', frame_layout2)]
]

window = sg.Window('串口调试工具', Layout)
dict_butten = {
	'打开串口':'-OPEN_GORGE-',
    '关闭串口':'-CLOSE_GORGE-',
    '发送':'-SEND_DATA-',
    '接收':'-RECIPT_DATA-',
    '清除发送数据':'-CLEAR_SENDDATA-',
    '清除接收数据':'-CLEAR_RECIPT-',
}

#实例化通信类
com = Communication('COM1', 9600, 6)
while True:
    event, values = window.read()
    if event==sg.WINDOW_CLOSED or event=='Exit':
        #退出
        break

    if event == '-OPEN_GORGE-':
        #打开串口
        com.open_gorge()

    if event == '-CLOSE_GORGE-':
        #关闭串口
        com.close_gorge()

    if event == '-SEND_DATA-':
        #发送数据
        templist = []
        result = com.send_messages(values['-INPUT_TEXT-'])
        templist.append(values['-INPUT_TEXT-'])
        window['-PB2-'].update(templist)

    if event == '-RECIPT_DATA-':
        #接收数据
        print("开始接收数据：")
        while True:
            # 一个字节一个字节的接收
            if com.ser.in_waiting:
                result = com.reception_messages_all()
                window['-PB3-'].update(result)
            else:
                window['-PB3-'].update(['没有接收到任何数据'])
                break

    if event == '-CLEAR_SENDDATA-':
        window['-PB2-'].update([])

    if event == '-CLEAR_RECIPT-':
        window['-PB3-'].update([])
    print(event)
    print(values)

window.close()

