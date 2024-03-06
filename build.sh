#!/bin/bash

rm -rf ./public ./content/gallery
mkdir -p ./content/gallery/my-data
mkdir -p ./content/gallery/other-data


# We have a clean gallery directory

python generate.py
