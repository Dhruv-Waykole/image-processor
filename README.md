The code works when OpenCV is not used and also when it is used.
def create_image(width, height, value=0 ) --> creates a image with its height and width.
def get_width(image) and def get_height(image) and def get_pixel(image,row,col): --> returns the width and height and the pixels of the image (for this task these values are given by the user)
def set_pixel(image,row,col,value) --> makes sure that a pixel doesn't exceed 255 value and writes the pixel value at that position.
def clamp(value) --> This functions clamps the value. Which means if value is less than 0 or more than 255, it sets the value to 0 and 255 respectively.
def print_image(image) --> helps to print the image
def invert(image) --> returns the new image after inverting it. This is done by subtracting the old pixel value from 255.
def brightness(image,amount) --> returns the new image with the required brightness chosen by the user.
def img_threshold(image, threshold) --> returns the a new image which is pure black and white. The clamp function plays a very important role here.
def flip_horizontal(image) and def flip_vertical(image) --> returns the new image flipped 90 degrees compared to the original
def flip(image) --> returns the new image flipped 180 degrees compared to the original
def crop(image, top, left, new_height, new_width) --> returns the cropped image by taking the required image size after cropping and the starting row and col to crop from as input given by the user.
def clamp_blur(value, low, high) and def get_pixel_clamped(image, row, col) --> These functions help to clamp the image borders 
def create_kernel(image, kernel) --> creates a small kernel for the image. It finds the kernel size using the height and width of the image, finds the divisor, which is required to perform the blur operation
How the blur operation works --> The code checks the neighboring pixel values for every pixel, sum them (gives the divisor) and the value of pixel for which it is currently applying the blur operation is divided by the divisor.
