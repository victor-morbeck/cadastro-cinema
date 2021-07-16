import PySimpleGUI as sg


""" Interfaces """

# configuração do tema da janela
sg.theme('DarkBrown4')

# definição das abas
aba_salas =   [ [ sg.Text('Gerenciamento de salas', size=(800,25)) ] ]

aba_pessoas = [ [ sg.Text('Gerenciamento de pessoas') ] ]

aba_sessoes = [ [ sg.Text('Gerenciamento de sessões') ] ]

# conteúdo da janela
layout = [  [sg.TabGroup([[
                sg.Tab('Salas', aba_salas), 
                sg.Tab('Pessoas', aba_pessoas), 
                sg.Tab('Sessões', aba_sessoes)]])],
            [sg.Button("Sair")]  ]

# criação da janela
janela = sg.Window('Cine Tão Tão Distante', layout, size=(1000, 500))

# laço para processar EVENTOS e receber VALORES de entrada
while True:
    evento, valores = janela.read()
    
    # se o usuário fechar a tela ou clicar em SAIR
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break