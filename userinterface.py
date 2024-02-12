import PySimpleGUI as sg

# Creating the Layout Object
layout = [[sg.Text("Olá!! Por favor cadastre-se")],
          [sg.Text("Insira o e-mail de login"), sg.Input()],
          [sg.Text("Insira a senha:"), sg.Input(key='Password', password_char="*")],
          [sg.Text("Insira o link do site:"), sg.Input()],
          [sg.Button("OK"), sg.Button("Cancelar")]]

# Main window configuration!
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()


"""
print("Arquivo não encontrado! Favor recadastre-se.")
login = input("Insira o e-mail de login: ")
password = input("Insira a senha: ")
website1 = input("Insira o site-base: ")
website2 = input("Insira o site-suporte (página de abrir processos): ")
data = {'login': login, 'senha': password, 'site1': website1, 'site2': website2}
"""
