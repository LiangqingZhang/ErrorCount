import pickle
from model import Model
import sys
modeltype=int(sys.argv[1])
print("modeltype: ",modeltype)

newres = pickle.load(open("data.pkl","rb"))
model = Model(newres)
res = model.forward(modeltype)
pickle.dump(res,open("res.pkl","wb"))