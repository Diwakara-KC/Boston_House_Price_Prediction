import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataset=load_boston()
df=pd.DataFrame(dataset.data)
df.columns=dataset.feature_names
df['Price']=dataset.target
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
r2score=r2_score(y_test,y_pred)

print(r2score)


import pickle
#pickle_out =pickle.load(reg,"Boston House44.pkl",'wb')
pickle.dump(reg,open("Boston_House_Prediction.pkl",'wb'))


