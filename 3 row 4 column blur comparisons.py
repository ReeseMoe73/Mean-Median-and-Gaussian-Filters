import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('Mod4CT1.jpg')

# Create 12 various blur types
img1 = cv2.blur(img, (3, 3))                                # Mean 3x3
img2 = cv2.medianBlur(img, 3)                               # Median 3x3
img3 = cv2.GaussianBlur(img, (3, 3), 5)                     # Gaussian 3x3, σ=5
img4 = cv2.GaussianBlur(img, (3, 3), 7)                     # Gaussian 3x3, σ=7
img5 = cv2.blur(img, (5, 5))                                # Mean 5x5
img6 = cv2.medianBlur(img, 5)                               # Median 5x5
img7 = cv2.GaussianBlur(img, (5, 5), 5)                     # Gaussian 5x5, σ=5
img8 = cv2.GaussianBlur(img, (5, 5), 7)                     # Gaussian 5x5, σ=7
img9 = cv2.blur(img, (7, 7))                                # Mean 7x7
img10 = cv2.medianBlur(img, 7)                              # Median 7x7
img11 = cv2.GaussianBlur(img, (7, 7), 5)                    # Gaussian 7x7, σ=5
img12 = cv2.GaussianBlur(img, (7, 7), 7)                    # Gaussian 7x7, σ=7


# Create 3x4 subplot grid
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(25, 5))
imgs = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]
titles = [
    'Mean Blur 3x3',
    'Median Blur 3x3',
    'Gaussian Blur 3x3 σ=5',
    'Gaussian Blur 3x3 σ=7',
    'Mean Blur 5x5',
    'Median Blur 5x5',
    'Gaussian Blur 5x5 σ=5',
    'Gaussian Blur 5x5 σ=7',
    'Mean Blur 7x7',
    'Median Blur 7x7',
    'Gaussian Blur 7x7 σ=5'
    'Gaussian Blur 7x7 σ=7'
]

# Move to subplots
for ax, im, title in zip(axs.flatten(), imgs, titles):
    ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
