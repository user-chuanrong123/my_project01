"""
串口调试界面
"""
import log
import PySimpleGUI as sg
from settings import GORGE_ARRAY
from settings import DEFAULT_GORGE
from settings import SELSIZE
from settings import BAUD_ARRAY
from settings import DEFAULT_SIZE
from settings import FONT_AND_SIZE
from settings import FONT_BUT_SIZE


Layout_Frame1 = [
    # [sg.Text('串口号:', font=FONT_AND_SIZE), sg.Combo(GORGE_ARRAY, font=FONT_AND_SIZE, key='-GORGE_NUMBER-', default_value=DEFAULT_GORGE, size=SELSIZE)],
    # [sg.Text('波特率:', font=FONT_AND_SIZE), sg.Combo(BAUD_ARRAY, font=FONT_AND_SIZE, key='-BAUD_NUMBER-', default_value=DEFAULT_SIZE, size=SELSIZE)],
    # [sg.Text('校验位:', font=FONT_AND_SIZE), sg.Combo(['无校验位'], font=FONT_AND_SIZE, key='-PARITY_BIT-', default_value='无校验位', size=SELSIZE)],
    # [sg.Text('数据位:', font=FONT_AND_SIZE), sg.Combo(['5', '6', '7', '8'], font=FONT_AND_SIZE, key='-DATA_BIT-', default_value='8', size=SELSIZE)],
    # [sg.Text('停止位:', font=FONT_AND_SIZE), sg.Combo(['1', '2', '3', '4'], font=FONT_AND_SIZE, key='-STOP_BIT-', default_value='1', size=SELSIZE)],
    # [sg.Button('打开串口', font=FONT_BUT_SIZE, key='-OPEN_BUTTEN-'), sg.Button('关闭串口', font=FONT_BUT_SIZE, key='-CLOSE_BUTTEN-')],
    # [sg.Button('发送', font=FONT_BUT_SIZE), sg.Input(font=FONT_AND_SIZE, key='-INPUT_TEXT-')],
    # [sg.Button('接收', font=FONT_BUT_SIZE)]
    sg.Text(''),
    sg.Listbox('', size=(40, 10), key='-PB1-')
]
Layout_Frame2 = [
    sg.Text(''),
    sg.Listbox('', size=(40,10), key='-PB2-')
]
###整体布局###
# layout = [
#     [sg.Text('串口号:', font=FONT_AND_SIZE), sg.Combo(GORGE_ARRAY, font=FONT_AND_SIZE, key='-GORGE_NUMBER-', default_value=DEFAULT_GORGE, size=SELSIZE), sg.Text('发送数据:', font=FONT_AND_SIZE), sg.Button('清除发送数据', font=FONT_BUT_SIZE, key='-CLEARBUTTER-')],
#     [sg.Text('波特率:', font=FONT_AND_SIZE), sg.Combo(BAUD_ARRAY, font=FONT_AND_SIZE, key='-BAUD_NUMBER-', default_value=DEFAULT_SIZE, size=SELSIZE)],
#     [sg.Text('校验位:', font=FONT_AND_SIZE), sg.Combo(['无校验位'], font=FONT_AND_SIZE, key='-PARITY_BIT-', default_value='无校验位', size=SELSIZE)],
#     [sg.Text('数据位:', font=FONT_AND_SIZE), sg.Combo(['5', '6', '7', '8'], font=FONT_AND_SIZE, key='-DATA_BIT-', default_value='8', size=SELSIZE)],
#     [sg.Text('停止位:', font=FONT_AND_SIZE), sg.Combo(['1', '2', '3', '4'], font=FONT_AND_SIZE, key='-STOP_BIT-', default_value='1', size=SELSIZE)],
#     [sg.Button('打开串口', font=FONT_BUT_SIZE, key='-OPEN_BUTTEN-'), sg.Button('关闭串口', font=FONT_BUT_SIZE, key='-CLOSE_BUTTEN-')],
#     [sg.Button('发送', font=FONT_BUT_SIZE), sg.Input(font=FONT_AND_SIZE, key='-INPUT_TEXT-')],
#     [sg.Button('接收', font=FONT_BUT_SIZE)]
# ]

layout = [
    [sg.Frame('1', Layout_Frame1), sg.Frame('2', Layout_Frame2)]
]
try:
    window = sg.Window('串口调试工具', layout)
except Exception as ex:
    log.error(ex)
while True:
    event, values = window.read()
    if event==sg.WINDOW_CLOSED or event=='Exit':
        break
    print(event)
    print(values)
window.close()
