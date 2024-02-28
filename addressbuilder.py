# This code fetches data from a client and builds a standard message,
# returning it along with all acquired info, in a dictionary format.

# Imports
import pandas as pd


def get_clientdata(cdie):
    # Building a pandas dataframe from the base sheet and filtering the required client.
    cdie_df = pd.read_excel("workbooks/cdie2address.xlsx")
    cdie_selection = cdie_df.loc[cdie_df['CDIE'] == cdie]

    # The selected line is then used on building a dictionary.
    client_info = {
        'code': cdie_selection['CDIE'].values[0],
        'name': cdie_selection['Nome'].values[0],
        'street': cdie_selection['Rua'].values[0],
        'number': cdie_selection['Número'].values[0],
        'neighborhood': cdie_selection['Bairro'].values[0],
        'city': cdie_selection['Município'].values[0],
        'postalcode': cdie_selection['CEP'].values[0],
        'region': cdie_selection['Região'].values[0]
    }

    # Dictionary variables are used on building a standard message.
    clientmessage = (f"Dados do cliente: \n"
                     f"{client_info['code']} - {client_info['name']} \n"
                     f"Endereço: {client_info['street']}, Nº {client_info['number']} – "
                     f"CEP: {client_info['postalcode']} \n"
                     f"Bairro: {client_info['neighborhood']}, {client_info['city']} \n"
                     f"Zona: {client_info['region']}")

    # Dictionary + Message are returned
    return client_info, clientmessage


info, text = get_clientdata(691969)
print(info)
print(text)
