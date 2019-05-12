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
col = db["data"]

findData = col.find()
train_data = []
for data in findData:
    train_data.append([np.array(data["spectrum"]),data["vectorA"]])
    #print("vectorA" + str(data["vectorA"]))
    #print("-----------------------------\n")

tr_spec_data = np.array([i[0] for i in train_data]) #store spectrogram in array
tr_vectorA_data = np.array([i[1] for i in train_data]) #store vectorA in array

model = Sequential()
# For the first layer, specify the input dimension
model.add(Dense(units = 30, input_dim = 1024))
# Specify an activation function
model.add(Activation('sigmoid'))
# For subsequent layers, the input dimension is presumed from
# the previous layer
model.add(Dense(units = 60))
model.add(Activation('sigmoid'))
model.add(Dense(units= 30 ))
model.add(Activation('softmax'))

optimizer = Adam(lr=1e-3)

model.compile(optimizer = optimizer, loss= 'categorical_crossentropy', metrics=['accuracy'])
model.fit(x= tr_spec_data, y= tr_vectorA_data, epochs=500, batch_size=100)
model.summary()