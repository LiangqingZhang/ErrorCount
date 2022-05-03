import numpy as np
import torch

class Model():
    def __init__(self,data):
        self.data = data
    
    def build_model1(self,x):
        result = -0.156+0.054*x[1]-0.006*x[1]**2+2.059*x[4]-0.813*x[1]*x[4]+0.088*(x[1]**2)*x[4]
        result += 0.049*x[7]+0.047*x[8]+0.067*x[9]+0.132*x[10]
        result += 0.046*x[11]+0.029*x[12]+0.013*x[13]+0.024*x[14]+0.03*x[15]+0.043*x[16]+0.052*x[17]+0.056*x[18]+0.052*x[18]+0.042*x[19]
        result += 0.003*x[2]-0.024*x[3]+0.012*x[6]
        return np.exp(result)-1

    def build_model2(self,x):
        result = 1.392-0.679*x[1]+0.075*x[1]**2-1.803*x[5]+0.496*x[1]*x[5]-0.057*(x[1]**2)*x[5]
        result += 0.044*x[7]+0.02*x[8]+0.032*x[9]+0.118*x[10]
        result += 0.047*x[11]+0.03*x[12]+0.012*x[13]+0.027*x[14]+0.039*x[15]+0.049*x[16]+0.053*x[17]+0.05*x[18]+0.038*x[18]+0.03*x[19]
        result += 0.009*x[2]-0.023*x[3]+0.502*x[6]
        return np.exp(result)-1
    
    def forward(self,modeltype):
        ress = []
        if(modeltype==1):
            for e in self.data:
                ress.append(self.build_model1(e))
        else:
            for e in self.data:
                ress.append(self.build_model2(e))
        return np.array(ress)
        