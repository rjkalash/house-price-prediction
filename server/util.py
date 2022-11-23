import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    print('loading saved artifacts ... start')
    global __data_columns
    global __locations
    global __model
    with open('F:\\Programs\\PythonWork\\jupyter_work\\bhp\server\\arifacts\\columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open('F:\\Programs\\PythonWork\\jupyter_work\\bhp\\server\\arifacts\\homePricePredictionModel.pickle','rb') as f:
        __model = pickle.load(f)
load_saved_artifacts()
def get_location_names():
   

    return __locations

def get_estimated_price(location,sqft,bhk, bath):
   
    try:
        li = __data_columns.index(location.lower())
        
    except: 
        li = -1

    x = np.zeros(len(__data_columns))
    x[0]= sqft
    x[1]=bhk
    x[2]=bath
    if li >=0:
        x[li] =1
    return round(__model.predict([x])[0],2)

if __name__=='__main__':
    print(get_location_names())
    print(get_estimated_price('Electronic City Phase II',1900, 4, 2))
    print(get_estimated_price('Electronic City Phase II',2000, 3, 2))
    print(get_estimated_price('it world',1900, 4, 2))