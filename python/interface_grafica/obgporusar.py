import pyautogui
import os
import time
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

linhas = [[sg.Text('Obbrigado por usar!')], [
    sg.Text('voce ja pode fechar essa pagina')]]

janela = sg.Window('bem vindo KKKKKKKKKKK', linhas)

while True:
    eventos, valores = anela = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
