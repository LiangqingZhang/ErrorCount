import numpy as np
import torch

class Model():
    def __init__(self,data,path):
        self.data = data
        self.parameters_model1 = np.array(list(np.load(path, allow_pickle=True).item()['model1'].values()))

        self.parameters_model2 = np.array(list(np.load(path, allow_pickle=True).item()['model2'].values()))
    def build_model1(self,x,p):


        result = p[0]+p[1]*x[1]+p[2]*x[1]**p[3]+p[4]*x[4]+p[5]*x[1]*x[4]+p[6]*(x[1]**p[7])*x[4]
        result += p[8]*x[7]+p[9]*x[8]+p[10]*x[9]+p[11]*x[10]
        result += p[12]*x[11]+p[13]*x[12]+p[14]*x[13]+p[15]*x[14]+p[16]*x[15]+p[17]*x[16]+p[18]*x[17]+p[19]*x[18]+p[20]*x[18]+p[21]*x[19]
        result += p[22]*x[2]+p[23]*x[3]+p[24]*x[6]
        return np.exp(result)-1

    def build_model2(self,x,p):
        result = p[0]+p[1]*x[1]+p[2]*x[1]**p[3]+p[4]*x[4]+p[5]*x[1]*x[4]+p[6]*(x[1]**p[7])*x[4]
        result += p[8]*x[7]+p[9]*x[8]+p[10]*x[9]+p[11]*x[10]
        result += p[12]*x[11]+p[13]*x[12]+p[14]*x[13]+p[15]*x[14]+p[16]*x[15]+p[17]*x[16]+p[18]*x[17]+p[19]*x[18]+p[20]*x[18]+p[21]*x[19]
        result += p[22]*x[2]+p[23]*x[3]+p[24]*x[6]
        return np.exp(result)-1
    
    def forward(self,modeltype):
        ress = []
        if(modeltype==1):
            for e in self.data:
                ress.append(self.build_model1(e,self.parameters_model1))
        else:
            for e in self.data:
                ress.append(self.build_model2(e,self.parameters_model2))
        return np.array(ress)
        
