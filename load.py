import os
import pandas as pd

def load_data_from_excel(name:str='database.xlsx'):
    database = pd.read_excel(os.path.join('data', name))
    database = database.filter([
        'Présence NASH         Non: 0 Oui: 1',
        'Pourcentage stéatose',
        'Inflammation lobulaire'],
        axis='columns')
    database = database.rename({
        'Présence NASH         Non: 0 Oui: 1':'Forme grave',
        'Stéatose':'Pourcentage stéatose',
        'Inflammation lobulaire':'Inflammation lobulaire'
    })
    database = database.dropna()
    return database

if __name__ == "__main__":
    print(load_data_from_excel())