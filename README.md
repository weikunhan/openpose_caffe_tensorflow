# openpose_tensorflow_caffe
--------------------------------------------------------------------------------

## Introduction
This partial research project for the Center for Vision, Cognition, Learning, and 
Autonomy (VCLA) lab by Professor. Song-Chun Zhu. In this Deep Neural Network (DNN)
Compression and Acceleration project, we pruning deep learning model to remove 
redundant connections in DNN. The contribution of this partial project are:

* established convertors between Caffe and Keras model convertingl;
* create a fune-tuning python script for Kers model fune-tune.

For more problem details, please go to
[my personal website](https://weikunhan.github.io).

## Requirements and Dependencies
Recommended use Anaconda to create the individual environment for this project 
and use following code to install dependencies:
```
conda install -c conda-forge tensorflow 
conda install -c conda-forge keras
conda install -c conda-forge opencv 
```
The following packages are required (the version numbers that have been tested 
are given for reference):
 
* Ptyhon 3.6
* Keris 2.1.5
* Tensorflow 1.5.0
* Numpy 1.14.2
* SciPy 1.0.1
* H5py 2.7.1
* OpenCV 3.4.1
* Caffe 1.0.0 (please see install_caffe.sh for installing Caffe)
* COCO (please see install_coco.sh for installing COCO API)
