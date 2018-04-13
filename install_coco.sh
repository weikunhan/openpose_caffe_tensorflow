#!/bin/sh

# This script for downloading COCO API and installing COCO API by conda
# You need use conda to create your project environment first by
# conda creat -n YOUR_PROJECT_ENVIRONMENT_NAME

echo "Downloading COCO Datasets API..."
git clone https://github.com/pdollar/coco.git

echo "Installing COCO Datasets API..."
source activate openpose_tensorflow
cd coco/PythonAPI
python3 setup.py install
cd ../../
