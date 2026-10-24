import cv2 as cv
import numpy as np
import processor as p

cv_img = cv.imread("/home/dhruv/Desktop/Photos/road2.jpeg", cv.IMREAD_GRAYSCALE)
if cv_img is None:
    raise FileNotFoundError("Could not read the image, check the path")

cv_img = cv.resize(cv_img, (200, 200))   # resize BEFORE converting
my_img = cv_img.tolist()
print("Size:", p.get_width(my_img), "x", p.get_height(my_img))

inverted = p.invert(my_img)
blurred = p.create_kernel(my_img, p.blur_kernel)
flipped = p.flip_horizontal(my_img)

new_height = int(input("Enter height needed for the cropped image: "))
new_width = int(input("Enter width needed for the cropped image: "))
print("Starting row can be 0 to", p.get_height(my_img) - new_height)
print("Starting col can be 0 to", p.get_width(my_img) - new_width)
top = int(input("starting row: "))
left = int(input("starting col: "))

cropped = p.crop(my_img, top, left, new_height, new_width)

cv.imwrite("original.png", cv_img)
cv.imwrite("inverted.png", np.array(inverted, dtype=np.uint8))
cv.imwrite("blurred.png", np.array(blurred, dtype=np.uint8))
cv.imwrite("flipped.png", np.array(flipped, dtype=np.uint8))
cv.imwrite("cropped.png", np.array(cropped, dtype=np.uint8))


cv.imshow("Cropped", np.array(cropped, dtype=np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()
