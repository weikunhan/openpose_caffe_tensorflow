#!/bin/sh

# This script for downloading trained Caffe model for paper 
# Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields
# https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation

echo "Downloading .caffemodel file..."
wget -nc --directory-prefix=./caffe/ http://posefs1.perception.cs.cmu.edu/Users/ZheCao/pose_iter_440000.caffemodel

echo "Downloading .prototxt file..."
wget -nc --directory-prefix=./caffe/ https://raw.githubusercontent.com/ZheC/Realtime_Multi-Person_Pose_Estimation/master/model/_trained_COCO/pose_deploy.prototxt
