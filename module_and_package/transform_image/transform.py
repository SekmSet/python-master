import cv2
import matplotlib.pyplot as plt

img = cv2.imread("obrigada_original.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX = 0, sigmaY = 0)

final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
plt.figure(figsize=(8, 8))
plt.imshow(final, cmap = "gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.show()