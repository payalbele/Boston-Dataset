
import pickle
import json
import numpy as np
import config 

class Boston():
    def __init__(self,CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def get_predicted(self):
        self.load_model()
        
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.CRIM
        test_array[1] = self.ZN
        test_array[2] = self.INDUS
        test_array[3] = self.CHAS
        test_array[4] = self.NOX
        test_array[5] = self.RM
        test_array[6] = self.AGE
        test_array[7] = self.DIS
        test_array[8] = self.RAD
        test_array[9] = self.TAX
        test_array[10] = self.PTRATIO
        test_array[11] = self.B
        test_array[12] = self.LSTAT
        predicted = self.model.predict([test_array])
        return predicted
    
        print("Test array :",test_array)
        
if __name__ == "__main__":
    CRIM= 0.00687
    ZN=19.0
    INDUS=3.21
    CHAS=0.0
    NOX=0.469
    RM=7.185
    AGE=69
    DIS=6.06
    RAD=3.0
    TAX=273.0
    PTRATIO=18.7
    B=396.90
    LSTAT=5.64

    boston = Boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)
    boston.get_predicted()
                    