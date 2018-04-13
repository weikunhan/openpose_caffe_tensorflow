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
KERAS_OUTPUT_DIR = 'keras/pose.h5'

# Get the skeleton of the Keras model
model = get_testing_model()

# Loop over all layers 
for layer in model.layers:

    # Extract each layer name
    layer_name = layer.name
    
    # Set all weights and biases from Caffe model into Keras model 
    if (os.path.exists(os.path.join(CAFFE_LAYERS_DIR, 
                                    'w_{:s}.npy'.format(layer_name))):
        w = np.load(os.path.join(CAFFE_LAYERS_DIR, 
                                 'w_{:s}.npy'.format(layer_name)))
        b = np.load(os.path.join(CAFFE_LAYERS_DIR, 
                                 'b_{:s}.npy'.format(layer_name)))
        
        # Tranfer the right form to store
        w = np.transpose(w, (2, 3, 1, 0))
        
        # Store into Keras model
        layer_weights = [w, b]
        layer.set_weights(layer_weights)

# Output Keras model
model.save_weights(KERAS_OUTPUT_DIR)

print('-------------------------Finished converting---------------------------')
