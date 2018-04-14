# -*- coding: utf-8 -*-
""" Caffe to Keras

This module can set dumped information from Caffe model into Keras model. You 
need first excute dump_caffe_layars.py to dumpe and store all information from
Caffe model.

################################################################################
# Author: Weikun Han <weikunhan@gmail.com>
# Crate Date: 04/12/2018
# Update:
# Reference: 
#   https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation
################################################################################
"""

import numpy as np
import os
from model import get_testing_model

# Please modify input path to locate you file
CAFFE_LAYERS_DIR = 'caffe/layers'
KERAS_DIR = 'keras'

# Setup input and output name
keras_model_filename = 'pose_iter_440000.h5'

# Get the skeleton of the Keras model
model = get_testing_model()

# Loop over all layers 
for layer in model.layers:
    
    # Set all weights and biases from Caffe model into Keras model 
    if os.path.exists(os.path.join(CAFFE_LAYERS_DIR, 
                                   'w_{:s}.npy'.format(layer.name))):
        w = np.load(os.path.join(CAFFE_LAYERS_DIR, 
                                 'w_{:s}.npy'.format(layer.name)))
        b = np.load(os.path.join(CAFFE_LAYERS_DIR, 
                                 'b_{:s}.npy'.format(layer.name)))
        
        # Tranfer the right form to store
        w = np.transpose(w, (2, 3, 1, 0))
        
        # Store into Keras model
        layer_weights = [w, b]
        layer.set_weights(layer_weights)

# Output Keras model
keras_model = os.path.join(KERAS_DIR, keras_model_filename)
model.save(keras_model)

print('-------------------------Finished converting---------------------------')
