import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the grayscale image
image = cv2.imread("Datasets/gnkgo/label/val/mastectomy_190.png", 0)  # Read as grayscale

# Transform 1 to 255
transformed_image = image * 255  # Converts 1 to 255, keeps 0 unchanged
if np.any(image):
    print("The image contains non-zero values.")
else:
    print("The image contains only zeros.")

# Display the transformed image
plt.imshow(transformed_image, cmap='gray')  # Use grayscale colormap
plt.title("Transformed Image")
plt.axis("off")  # Hide axis
plt.show()  # Display the image
