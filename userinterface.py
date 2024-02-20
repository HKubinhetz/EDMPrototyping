import PySimpleGUI as sg

# Defining the Theme
sg.theme('SystemDefault')

# Creating the Form Layout Object
# TODO - If this is not the first time form_layout runs, use previous keys as values.

form_layout = [[sg.VPush()],
               [sg.Text("Olá!! Por favor cadastre-se:", pad=(0, 20))],
               [sg.Text("Insira o e-mail de login"), sg.Push(), sg.Input(key='login', size=(50, 1))],
               [sg.Text("Insira a senha:"), sg.Push(), sg.Input(key='password', password_char="*", size=(50, 1))],
               [sg.Push(), sg.Button("OK", key="submit", size=(20, 100), pad=(0, 20)), sg.Push()],
               [sg.VPush()]]


def run_form():
    # Creating an empty dictionary
    data = {}

    # Main window configuration!
    form_window = sg.Window("Cadastro", form_layout, size=(600, 220), finalize=True)
    form_window["login"].bind("<Return>", "_Enter")
    form_window["password"].bind("<Return>", "_Enter")

    # Create an event loop
    while True:
        event, values = form_window.read()
        # End program if user closes window, presses the OK button or presses enter on the keyboard.
        if (event == "OK" or event == "_enter" or event == sg.WIN_CLOSED or
                event == "login" + "_Enter" or event == "password" + "_Enter"):

            data["login"] = values["login"]
            data["senha"] = values["password"]
            form_window.close()

            # TODO - If any key is empty, show a warning and ask for input again

            return data

