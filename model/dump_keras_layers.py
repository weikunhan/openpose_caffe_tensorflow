# -*- coding: utf-8 -*-
""" Dump Keras layers
This module dumped information from Keras model. 
################################################################################
# Author: Weikun Han <weikunhan@gmail.com>
# Crate Date: 04/12/2018
# Update:
# Reference: 
################################################################################
"""

import numpy as np
import os
from keras.models import load_model

# Please modify input path to locate you file
KERAS_DIR = 'keras'
LAYERS_OUTPUT = 'keras/layers'

# Check location to save datasets
if not os.path.exists(LAYERS_OUTPUT):
    os.makedirs(LAYERS_OUTPUT)

# Input Keras model
keras_model_filename = 'pose_iter_440000.h5'

# Load Keras model
keras_model = os.path.join(KERAS_DIR, keras_model_filename)
model = load_model(keras_model)

# Check for each layer name and each input data shapes 
for layer in model.layers:
      
    print('{:<5}:  {}'.format(layer.name, layer.input_shape))

print('------------------------Beginning dumping------------------------------')

# Write out weight matrices and bias vectors
for layer in model.layers:
    if len(layer.get_weights()) is 2:
        np.save(os.path.join(LAYERS_OUTPUT, "w_{:s}.npy".format(layer.name)), 
                layer.get_weights()[0])
        np.save(os.path.join(LAYERS_OUTPUT, "b_{:s}.npy".format(layer.name)), 
                layer.get_weights()[1])
      
        print('{:<5}:  weight-{} bias-{}'.format(layer.name, 
                                                 layer.get_weights()[0], 
                                                 layer.get_weights()[1]))
                                                 
    else:
        np.save(os.path.join(LAYERS_OUTPUT, "w_{:s}.npy".format(layer.name)), 0)
        np.save(os.path.join(LAYERS_OUTPUT, "b_{:s}.npy".format(layer.name)), 0)

print('-------------------------Finished dumping------------------------------')
