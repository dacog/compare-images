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

Modify the folder paths in the script

```python
folder1 = './f1'
folder2 = './f2'
```
run the script

```bash
python compare.py
```

output is the following, per image

```shell
Similarity for Screenshot 2022-01-18 095344.png: 1.00
Similarity for Screenshot 2022-01-18 095344.png - SSIM: 1.00, Color: 1.00
Image 1 DPI: (95.9866, 95.9866), Size: (1472, 854)
Image 2 DPI: (95.9866, 95.9866), Size: (1472, 854)
Print Comparison for Screenshot 2022-01-18 095344.png: Resolution and size match.
```


## TO-DO (maybe)

- [ ] print only images that are not equal
- [ ] use arguments for folder-paths
- [ ] allow ocmparison of 2 folders with different files in them, and print which files are not present in each folder.
