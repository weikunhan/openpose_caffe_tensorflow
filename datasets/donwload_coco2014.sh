#!/bin/bash

# donwload COCO datasets 2014 train, 2014 test, 2014 validation, 2014 annotations
# Note: Better use google chrome download, it is faster (and mamually unzip)!

mkdir train_coco2014
mkdir validation_coco2014
mkdir test_coco2014
mkdir annotations_coco2014

echo "Downloading train datasets 2014..."
#wget http://msvocds.blob.core.windows.net/coco2014/train2014.zip

echo "Downloading validation datasets 2014..."
#wget http://msvocds.blob.core.windows.net/coco2014/val2014.zip

echo "Downloading test datasets 2014..."
#wget http://msvocds.blob.core.windows.net/coco2014/test2014.zip

echo "Downloading annotations datasets 2014..."
wget http://msvocds.blob.core.windows.net/annotations-1-0-3/person_keypoints_trainval2014.zip

echo "Unzipping annotations datasets 2014..."
unzip person_keypoints_trainval2014.zip -d annotations_coco2014

echo "Unzipping test datasets 2014..."
#unzip test2014.zip -d test_coco2014

echo "Unzipping validation datasets 2014..."
#unzip val2014.zip -d validation_coco2014

echo "Unzipping train datasets 2014..."
#unzip train2014.zip -d train_coco2014

rm -f person_keypoints_trainval2014.zip
#rm -f test2014.zip
#rm -f train2014.zip
#rm -f val2014.zip
