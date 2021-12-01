#!/usr/bin/bash
# Script to download and extract data
# Data is imagenette, which is a subset of the ImageNet dataset
# More info can be found here: https://github.com/fastai/imagenette
set -e # exit script upon failure

wget https://s3.amazonaws.com/fast-ai-imageclas/imagewoof2-320.tgz 
file_path=$(realpath $0)
data_path=$file_path/../data
echo data_path
if [ ! -d $data_path ]; then
    mkdir $data_path 
fi
mv imagenette2.tgz $data_path/imagenette2.tgz
tar xvf $data_path/imagenette2.tgz
rm imagenette2.tgz
