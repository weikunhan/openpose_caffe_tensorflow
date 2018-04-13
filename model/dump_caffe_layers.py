# -*- coding: utf-8 -*-
""" Dump Caffe layers

This module dumped information from Caffe model. 

################################################################################
# Author: Weikun Han <weikunhan@gmail.com>
# Crate Date: 04/13/2018
# Update:
# Reference: 
################################################################################
"""

import caffe
import numpy as np
import os

# Please modify input path to locate you file
CAFFE_DIR = 'model/caffe/'
LAYERS_OUTPUT = 'model/caffe/layers'

# Input Caffe model
caffe_model = os.path.join(CAFFE_DIR, 'pose_iter_440000.caffemodel')
caffe_proto = os.path.join(CAFFE_DIR, 'pose_deploy.prototxt')

# Initial Caffe network
caffe.set_mode_cpu()
net = caffe.Net(caffe_proto, caffe_model, caffe.TEST)

# Check for each layer name and each input data shapes 
for name, blob in net.blobs.items():
    
    print('{:<5}:  {}'.format(name, blob.data.shape))

# Write out weight matrices and bias vectors
for name, param in net.params.items():
    np.save(os.path.join(LAYERS_OUTPUT, "w_{:s}.npy".format(name)), param[0].data)
    np.save(os.path.join(LAYERS_OUTPUT, "b_{:s}.npy".format(name)), param[1].data)
    
    print('{:<5}:  weight-{} bias-{}'.format(name, param[0].data.shape, param[1].data.shape))

print('-------------------------Finished dumping------------------------------')
