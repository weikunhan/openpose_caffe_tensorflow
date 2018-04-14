# -*- coding: utf-8 -*-
""" Keras to Caffe

This module can set dumped information from Keras model into Caffe model. You 
need first excute dump_keras_layars.py to dumpe and store all information from
Keras model.

################################################################################
# Author: Weikun Han <weikunhan@gmail.com>
# Crate Date: 04/12/2018
# Update: 04/14/2018
# Reference: 
################################################################################
"""

import numpy as np
import os
import caffe

# Please modify input path to locate you file
KERAS_LAYERS_DIR = 'keras/layers'
CAFFE_DIR = 'caffe'

# Setup input and output name
caffe_proto_filename = 'pose_deploy.prototxt'
caffe_model_filename = 'pose_iter_440000_convert.caffemodel'

# Setup the Caffe model
caffe_proto = os.path.join(CAFFE_DIR, caffe_proto_filename)
caffe.set_mode_cpu()
net = caffe.Net(caffe_proto, caffe.TEST)

# Loop over all layers 
for name, param in net.params.items():
    
    # Set all weights and biases from Caffe model into Keras model 
    if os.path.exists(os.path.join(KERAS_LAYERS_DIR, 
                                   'w_{:s}.npy'.format(name))):
        w = np.load(os.path.join(KERAS_LAYERS_DIR, 
                                 'w_{:s}.npy'.format(name)))
        b = np.load(os.path.join(KERAS_LAYERS_DIR, 
                                 'b_{:s}.npy'.format(name)))
        
        # Tranfer the right form to store
        w = np.transpose(w, (3, 2, 0, 1))
        
        # Store into Keras model
        net.params[name][0].data[...] = w
        net.params[name][1].data[...] = b

# Output Caffe model
caffe_model = os.path.join(CAFFE_DIR, caffe_model_filename)
net.save(caffe_model)

print('-------------------------Finished converting---------------------------')
