import os
import pandas as pd

def load_data_from_excel(name:str='database.xlsx'):
    db = pd.read_excel(os.path.join('data', name))
    db.dropna(inplace = True)
    db = db[db['Présence NASH']!=-1]
    db.reset_index(drop = True, inplace = True)
    return db

def database_preop(db:pd.DataFrame=load_data_from_excel()):
    cMax = db.columns.get_loc('CAP')
    dbPreop = db.iloc[:,0:cMax+1]
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
    dbPreop['Présence NASH'] = dbPreop.pop('Présence NASH')
    return dbPreop

def normalise(db):
    return()


if __name__ == "__main__":
    print(database_preop())