# Compare images in 2 folders

This script compares images in 2 folders and outputs the differences in a new folder.
It uses openCV and Pillow to compare the images, by using greyscale, color and size comparison.

## Install os dependencies

```bash
sudo apt-get update
sudo apt-get install libgl1-mesa-glx
```

## Install python dependencies

```bash
pip install -r requirements.txt
```

## Run the script

```bash
python compare.py
```