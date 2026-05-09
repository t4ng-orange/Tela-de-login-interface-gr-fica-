from PySimpleGUI import PySimpleGUI as sg

#layout

sg.theme = ('Reddit')

layout = [
    [sg.Text('usuario'),sg.Input(key = 'usuario')],
    [sg.Text('senha'),sg.Input(key = 'senha',password_char = "*"),],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('entrar')]
]

#gerar interface gráfica
janela = sg.Window('Tela de login',layout)
#ler os eventos

while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        if valores['usuario'] == "arthur" and valores['senha'] == '123456':
            print("Bem vindo sr arthur!")