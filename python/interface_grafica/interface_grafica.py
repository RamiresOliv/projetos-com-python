from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

linhas = [[sg.Text('Bem Vindo(a)')],
          [sg.Text('usuario:'), sg.Input(key='usuario')],
          [sg.Text('senha:'),
           sg.Input(key='senha', password_char='*')],
          [sg.Checkbox('quer mesmo salvar?')], [sg.Button("submit")]]

janela = sg.Window('bem vindo(a)', linhas)

while True:
    eventos, valores = anela = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        print('vlw por usar')
        break
    if valores['usuario'] == 'ramires' and valores['senha'] == '123':
        print('bem vindo ramires.')

    elif valores['usuario'] == 'arthur' and valores['senha'] == '123':
        print('bem vindo arthur.')
