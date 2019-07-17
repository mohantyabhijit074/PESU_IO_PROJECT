# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:45:24 2019

@author: Abhijit
 model.fit(x_train,y_train,epochs=5,batch_size=32)
Epoch 1/5
142193/142193 [==============================] - 4s 27us/sample - loss: 0.5444 - acc: 0.8085
Epoch 2/5
142193/142193 [==============================] - 4s 27us/sample - loss: 0.3903 - acc: 0.8338
Epoch 3/5
142193/142193 [==============================] - 4s 27us/sample - loss: 0.3718 - acc: 0.8413
Epoch 4/5
142193/142193 [==============================] - 4s 26us/sample - loss: 0.3681 - acc: 0.8424
Epoch 5/5
142193/142193 [==============================] - 4s 27us/sample - loss: 0.3656 - acc: 0.8435
val_loss,val_accu=model.evaluate(x_test,y_test)
28439/28439 [==============================] - 0s 16us/sample - loss: 0.3599 - acc: 0.8447
"""
import pandas as pd
import tensorflow as tf
mydataset=pd.read_csv('project.csv')
mydataset["RainToday"]=pd.Categorical(mydataset["RainToday"])
mydataset["RainToday"]=mydataset.RainToday.cat.codes
mydataset["RainTomorrow"]=pd.Categorical(mydataset["RainTomorrow"])
mydataset["RainTomorrow"]=mydataset.RainTomorrow.cat.codes
mydataset["WindGustSpeed"]=pd.Categorical(mydataset["WindGustSpeed"])
mydataset["WindGustSpeed"]=mydataset.WindGustSpeed.cat.codes
mydataset["Rainfall"]=pd.Categorical(mydataset["Rainfall"])
mydataset["Rainfall"]=mydataset.Rainfall.cat.codes
mydataset["WindGustDir"]=pd.Categorical(mydataset["WindGustDir"])
mydataset["WindGustDir"]=mydataset.WindGustDir.cat.codes
mydataset["WindSpeed9am"]=pd.Categorical(mydataset["WindSpeed9am"])
mydataset["WindSpeed9am"]=mydataset.WindSpeed9am.cat.codes
mydataset["WindSpeed3pm"]=pd.Categorical(mydataset["WindSpeed3pm"])
mydataset["WindSpeed3pm"]=mydataset.WindSpeed3pm.cat.codes
mydataset["Humidity9am"]=pd.Categorical(mydataset["Humidity9am"])
mydataset["Humidity9am"]=mydataset.Humidity9am.cat.codes
mydataset["Humidity3pm"]=pd.Categorical(mydataset["Humidity3pm"])
mydataset["Humidity3pm"]=mydataset.Humidity3pm.cat.codes
mydataset["Pressure9am"]=pd.Categorical(mydataset["Pressure9am"])
mydataset["Pressure9am"]=mydataset.Pressure9am.cat.codes
mydataset["Pressure3pm"]=pd.Categorical(mydataset["Pressure3pm"])
mydataset["Pressure3pm"]=mydataset.Pressure3pm.cat.codes
mydataset["Cloud9am"]=pd.Categorical(mydataset["Cloud9am"])
mydataset["Cloud9am"]=mydataset.Cloud9am.cat.codes
mydataset["Cloud3pm"]=pd.Categorical(mydataset["Cloud3pm"])
mydataset["Cloud3pm"]=mydataset.Cloud3pm.cat.codes
mydataset["Temp9am"]=pd.Categorical(mydataset["Temp9am"])
mydataset["Temp9am"]=mydataset.Temp9am.cat.codes
mydataset["Temp3pm"]=pd.Categorical(mydataset["Temp3pm"])
mydataset["Temp3pm"]=mydataset.Temp3pm.cat.codes
mydataset=mydataset.fillna(method="ffill")
final=mydataset.drop(["Date","Location","Evaporation","Sunshine","WindDir9am","WindDir3pm","RISK_MM"],axis="columns")
final.dtypes
final=final.fillna(method="ffill")
x=final[["WindGustSpeed","RainToday","Rainfall","WindGustDir","MinTemp","MaxTemp","WindSpeed9am","WindSpeed9am","WindSpeed3pm","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","Temp9am","Temp3pm"]]
y=final["RainTomorrow"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8)
x_train=final[["WindGustSpeed","RainToday","Rainfall","WindGustDir","MinTemp","MaxTemp","WindSpeed9am","WindSpeed9am","WindSpeed3pm","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","Temp9am","Temp3pm"]].values
y_train=final["RainTomorrow"].values
x_train=x_train.astype("float32")
y_train=y_train.astype("float32")
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu,input_shape=x_train.shape[1:]))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(22, activation=tf.nn.softmax))
model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5,batch_size=32)
val_loss,val_accu=model.evaluate(x_test,y_test)
print(val_loss,val_accu)

