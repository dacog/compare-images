import cv2
import numpy as np
from PIL import Image
import os

from skimage.metrics import structural_similarity as compare_ssim
import cv2

def compare_images(image1, image2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute the Structural Similarity Index (SSIM) between the two images
    score, diff = compare_ssim(gray1, gray2, full=True)
    return score

def compare_images_color(image1, image2):
    # Convert images to grayscale and compute SSIM
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    ssim_score, _ = compare_ssim(gray1, gray2, full=True)

    # Convert images to HSV for color histogram comparison
    hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # Calculating histograms (considering all channels) and normalize
    hist1 = cv2.calcHist([hsv1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Compare histograms using the Correlation method
    color_similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return ssim_score, color_similarity


def compare_for_print(image_path1, image_path2):
    # Load images using Pillow to check resolution
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Compare resolutions (DPI)
    dpi1 = img1.info.get('dpi', (72, 72))  # Defaulting to 72 DPI if not specified
    dpi2 = img2.info.get('dpi', (72, 72))
    
    # Compare sizes (dimensions)
    size1 = img1.size
    size2 = img2.size

    print(f"Image 1 DPI: {dpi1}, Size: {size1}")
    print(f"Image 2 DPI: {dpi2}, Size: {size2}")

    return dpi1 == dpi2 and size1 == size2

folder1 = './f1'
folder2 = './f2'

# Ensure both folders contain the same set of files
files1 = set(os.listdir(folder1))
files2 = set(os.listdir(folder2))
if files1 != files2:
    print("Folders do not contain the same files")
else:
    for filename in files1:
        img1 = cv2.imread(os.path.join(folder1, filename))
        img2 = cv2.imread(os.path.join(folder2, filename))

        similarity_score = compare_images(img1, img2)

        print(f"Similarity for {filename}: {similarity_score:.2f}")

        ssim_score, color_score = compare_images_color(img1, img2)
        print(f"Similarity for {filename} - SSIM: {ssim_score:.2f}, Color: {color_score:.2f}")

        filepath1 = os.path.join(folder1, filename)
        filepath2 = os.path.join(folder2, filename)

        print_comparison_result = compare_for_print(filepath1, filepath2)
        if print_comparison_result:
            print(f"Print Comparison for {filename}: Resolution and size match.")
        else:
            print(f"Print Comparison for {filename}: Resolution and/or size do not match.")
