import os
from numpy import NaN
import pandas as pd
from sklearn.impute import SimpleImputer

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
            'Metavir',
            'Biopsie hépatique',
            'Degré stéatose',
            'Pourcentage stéatose',
            'Ballonisation/clarification',
            'Inflammation lobulaire',
            'Score NAS',
            'Fibrose Kleiner'
            ],
            inplace = True)
    # dbPreop = dbPreop[[
    #     'Globules rouges',
    #     'Hémoglobine',
    #     'Albumine',
    #     'G-globulines',
    #     'FIBROMETA',
    #     'Index Triglycérides-glucose',
    #     'HOMA-IR',
    #     'QUICKI',
    #     'Index peptide C',
    #     'Elastométrie',
    #     'Acide urique',
    #     'Glycémie',
    #     'HbA1c',
    #     'Triglycérides',
    #     'ASAT',
    #     'ALAT',
    #     'GGT',
    #     'Ferritine',
    #     'Actitest',
    #     'Fibrotest',
    #     'Insuline',
    #     'Peptide C',
    #     'Dépense énergétique de repos',
    #     'Présence NASH'
    # ]]
    dbPreop = dbPreop[[
        'Age',
        'Sexe',
        'BilirubineT',
        'Elastométrie',
        'CAP',
        'Acide urique',
        'Triglycérides',
        'ASAT',
        'ALAT',
        'GGT',
        'Ferritine',
        'Dépense énergétique de repos',
        'HOMA-IR',
        'Présence NASH'
    ]]
    dbPreop['Présence NASH'] = dbPreop.pop('Présence NASH')
    return fill_nan(dbPreop)

def fill_nan(db):
    imputer = SimpleImputer(missing_values=-1, strategy='median')
    result_imputer = imputer.fit_transform(db)
    return pd.DataFrame(result_imputer, columns=db.columns)

def corr_to_excel():
    db = load_data_from_excel()
    db.drop(
        columns = [
            'Date naissance',
            'Date inclusion',],
            inplace = True)
    db = fill_nan(db)
    corr = db.corr()
    corr.style.background_gradient(cmap='coolwarm').set_precision(2).to_excel(r'D:\-CHARLES-\VSCodeProjects\SleeveProject\data\corrs.xlsx', index=False, header=True)
    return


if __name__ == "__main__":
    print(database_preop())