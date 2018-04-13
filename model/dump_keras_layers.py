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

import caffe
import numpy as np
import os
from keras.models import load_model

layers_output = 'model/keras/layers'
keras_model = 'model/keras/pose_iter_440000.h5'


model = load_model(keras_model)

# Loop over all layers 
for layer in model.layers:
      
    # Extract each layer name
    layer_name = layer.name

    # write out weight matrices and bias vectors
    print(layer_name, layer.get_weights()[0].shape, layer.get_weights()[1].shape)
    np.save(os.path.join(layers_output, "W_{:s}.npy".format(k)), layer.get_weights()[0])
    np.save(os.path.join(layers_output, "b_{:s}.npy".format(k)), layer.get_weights()[2])

print("Done !")
