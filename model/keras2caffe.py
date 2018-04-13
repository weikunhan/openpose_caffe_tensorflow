# -*- coding: utf-8 -*-
""" Keras to Caffe

This module can set dumped information from Keras model into Caffe model. You 
need first excute dump_keras_layars.py to dumpe and store all information from
Keras model.

################################################################################
# Author: Weikun Han <weikunhan@gmail.com>
# Crate Date: 04/12/2018
# Update:
# Reference: 
################################################################################
"""

import numpy as np
import os
import caffe

# Please modify input path to locate you file
KERAS_LAYERS_DIR = 'keras/layers'
CAFFE_INPUT_DIR = 'caffe/'
CAFFE_OUTPUT_DIR = 'caffe/pose_iter_440000_convert.caffemodel'

# Get the skeleton of the Caffe model
model_filename = 'pose_deploy.prototxt'
model = os.path.join(CAFFE_INPUT_DIR, model_filename)

# Setup the Caffe model
net = caffe.Net(model, caffe.TEST)

# Loop over all layers 
for layer_name, variable in net.params.items():
    
    # Set all weights and biases from Caffe model into Keras model 
    if (os.path.exists(os.path.join(KERAS_LAYERS_DIR, 
                                    'w_{:s}.npy'.format(layer_name))):
        w = np.load(os.path.join(KERAS_LAYERS_DIR, 
                                 'w_{:s}.npy'.format(layer_name)))
        b = np.load(os.path.join(KERAS_LAYERS_DIR, 
                                 'b_{:s}.npy'.format(layer_name)))
        
        # TODO: do we need transpose for caffe2keras?
        # Tranfer the right form to store
        #w = np.transpose(w, (2, 3, 1, 0))
        
        # Store into Keras model
        net.params[layer_name][0] = w
        net.params[layer_name][1] = b

# Output Caffe model
net.save(CAFFE_OUTPUT_DIR)

print('-------------------------Finished converting---------------------------')
