import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


##########
def separate_data(data, shuff:bool=False):
    X, y = separate_discriminant(data)
    X_train, X_test, y_train, y_test = separate_train_test(X, y, shuff)
    X_train, X_test = standard_scaling(X_train, X_test)
    new_data = (X_train, X_test, y_train, y_test)
    return new_data


###
def separate_discriminant(data):
    cMax = data.shape[1]
    X = data[:, 0:cMax-1]
    y = data[:, cMax-1]
    return(X, y)

def separate_train_test(X, y, shuff):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=shuff)
    return(X_train, X_test, y_train, y_test)

def standard_scaling(X_train, X_test):
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return(X_train, X_test)

###
def save_data(d):
    with open('mypicklefile', 'wb') as f1:
        pickle.dump(d, f1)
    return

def load_data():
    with open('mypicklefile', 'rb') as f1:
        d = pickle.load(f1)
    return d

def get_col_names():
    from load_data import database_preop
    col_names = database_preop().columns.values.tolist()
    return(col_names)

##########
if __name__ == "__main__":
    from load_data import database_preop
    data = database_preop().values
    col_names = get_col_names()
    new_data = separate_data(data, shuff=True)
    save_data(new_data)
    X_train, X_test, y_train, y_test = load_data()
    print("Separated datas successfully saved")