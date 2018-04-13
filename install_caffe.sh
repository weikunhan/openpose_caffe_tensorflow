#!/bin/sh

# This script for downloading Caffe and installing Caffe by conda
# You need use conda to create your project environment first by
# conda creat -n YOUR_PROJECT_ENVIRONMENT_NAME
# This project environment use another environment to avoid conflct with 
# tensorflow. Thus you need two environment, which different from install COCO 
# API. Moreover, in this environment, you need install Tensorflow and Kares for 
# converting between Kares and Caffe model

echo "Downloading Caffe..."
git clone https://github.com/BVLC/caffe.git

echo "Beginning install Caffe..."
source activate openpose_caffe

echo "Installing OpenCV..."
conda install -c menpo opencv

echo "Installing dependencies..."
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y build-essential cmake git pkg-config
sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev protobuf-compiler
sudo apt-get install -y libatlas-base-dev 
sudo apt-get install -y --no-install-recommends libboost-all-dev
sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev

echo "Installing Caffe..."
cd caffe
mkdir build 
cd build
cmake -D python_version=3 ..
make all
make install
make runtest

echo "Installing Caffe Python API..."
cd ../python
sed -i -e 's/python-dateutil>=1.4,<2/python-dateutil>=2.0/g' requirements.txt
for req in $(cat requirements.txt); do pip install $req; done
cd ../build
make pycaffe

echo "export PYTHONPATH={path to your caffe}/python/:$PYTHONPATH"

