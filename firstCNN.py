<<<<<<< HEAD
from __future__ import print_function
import numpy as np
from random import shuffle
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import *
from keras.layers import Dense, Activation
from keras.optimizers import *

#import matplotlib.pyplot as plt


from flask import Flask
from flask import request
from pymongo import MongoClient
import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client["test"]
col = db["data01"]

findData = col.find()
train_data = []
for data in findData:
    train_data.append([np.array(data["spectrum"]),data["vectorA"]])
    #print("vectorA" + str(data["vectorA"]))
    #print("-----------------------------\n")
    #print("data loaded")
print(train_data)
tr_spec_data = np.array([i[0] for i in train_data]) #store spectrogram in array
tr_vectorA_data = np.array([i[1] for i in train_data]) #store vectorA in array
print(tr_vectorA_data.shape)

model = Sequential()
# For the first layer, specify the input dimension
model.add(Dense(units = 512, input_dim = 1024))
# Specify an activation function
model.add(Activation('sigmoid'))
# For subsequent layers, the input dimension is presumed from
# the previous layer
model.add(Dense(units = 56))
model.add(Activation('sigmoid'))
model.add(Dense(units= 28 ))
model.add(Activation('sigmoid'))

optimizer = Adam(lr=1e-3)

model.compile(optimizer = optimizer, loss= 'mean_squared_error', metrics=['accuracy'])
model.fit(x= tr_spec_data, y= tr_vectorA_data, epochs=500, batch_size=100)


model.summary()