#!/bin/bash

# gpu, use cnmem
# export THEANO_FLAGS='device=gpu0,floatX=float32,lib.cnmem=0.9'

# cpu
export THEANO_FLAGS=device=cpu,floatX=float32
python -u ./train_sem.py > logb.txt 2>&1 &
