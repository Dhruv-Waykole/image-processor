def create_image(width, height, value=0 ):
    return [[value for _ in range(width)] for _ in range(height)]

def get_width(image):
    return len(image[0])

def get_height(image):
    return len(image)

def get_pixel(image,row,col):
    return image[row][col]

def set_pixel(image,row,col,value):
    if not 0 <= value <=255:
        raise ValueError("value must be in between 0 to 255")
    image[row][col] = value

def print_image(image):
    for row in image:
        print(" ".join(f"{pixel:3}" for pixel in row))

width = int(input("Enter width:"))
height = int(input("Enter height: "))
image = create_image(width, height)

for row in range(get_height(image)):
    for col in range(get_width(image)):
        set_pixel(image, row, col, 200)

print_image(image)