#!/bin/bash

set -euo pipefail

rm -rf ./public ./content/gallery ./static/gallery
mkdir -p ./content/gallery/my-data
mkdir -p ./content/gallery/other-data
mkdir -p ./static/gallery

# renovate: datasource=github-releases depName=USA-RedDragon/astro.garden-images
GALLERY_VERSION=11

curl -fSsL https://github.com/USA-RedDragon/astro.garden-images/releases/download/${GALLERY_VERSION}/gallery.tar.gz | tar -xz -C ./static/gallery
rm -rf ./static/gallery/my-data ./static/gallery/other-data ./static/gallery/my-data.json ./static/gallery/other-data.json

# We have a clean gallery directory
python generate.py
