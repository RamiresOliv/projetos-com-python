import pyautogui
import os
import time
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

linhas = [[sg.Text('Bem Vindo(a)')],
          [sg.Text('usuario:'), sg.Input(key='usuario')],
          [sg.Text('senha:'),
           sg.Input(key='senha', password_char='*')],
          [sg.Checkbox('quer mesmo salvar?')], [sg.Button("submit")]]

bemvindolinhas = [[sg.Text('bem vindo!')], [sg.Button("submit")]]

janela = sg.Window('bem vindo KKKKKKKKKKK', linhas)

bemvindojanela = sg.Window('bem vindo KKKKKKKKKKK', bemvindolinhas)

while True:
    eventos, valores = anela = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        print('vlw por usar')
        break
    if valores['usuario'] == 'ramires' and valores['senha'] == 'loramires':
        print('bem vindo ramires.')

        os.system('start oi.bat')
    elif valores['usuario'] == 'arthur' and valores['senha'] == '123':
        print('bem vindo arthur.')
