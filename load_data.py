import os
import pandas as pd

def load_data_from_excel(name:str='database.xlsx'):
    db = pd.read_excel(os.path.join('data', name))
    db.dropna(inplace = True)
    db = db[db['Présence NASH']!=-1]
    db.reset_index(drop = True, inplace = True)
    return db

def database_preop(database:pd.DataFrame=load_data_from_excel()):
    jMax = database.columns.get_loc('CAP')
    dbPreop = database.iloc[:,0:jMax+1]
    dbPreop.drop(
        columns = [
            'Date naissance',
            'Date inclusion',
            'Biopsie hépatique',
            'Degré stéatose',
            'Pourcentage stéatose',
            'Ballonisation/clarification',
            'Inflammation lobulaire',
            'Score NAS',
            'Fibrose Kleiner'
            ],
            inplace = True)
    return dbPreop

def normalise(db):
    return()


if __name__ == "__main__":
    print(database_preop())