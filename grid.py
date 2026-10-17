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

def clamp(value):
    if value < 0:
        return 0
    if value > 255:
        return 255
    
def print_image(image):
    for row in image:
        print(" ".join(f"{pixel:3}" for pixel in row))

def invert(image):
    new_pixel= 255-pixel   
    for row in range(get_height(image)):
     for col in range(get_width(image)):
        set_pixel(image, row, col, new_pixel)  
    return image       

def brightness(image):
    new_pixel=get_pixel(image,row,col)+amount
    for row in range(get_height(image)):
         for col in range(get_width(image)):
            set_pixel(image, row, col, new_pixel)  
    return (image, lambda amount: clamp(255+amount)) 

width = int(input("Enter width:"))
height = int(input("Enter height: "))
image = create_image(width, height)
pixel=int(input("Enter pixel : "))
amount = int(input("Enter amount:"))

for row in range(get_height(image)):
    for col in range(get_width(image)):
        set_pixel(image, row, col, pixel)
        

print_image(image)
print_image(invert(image))
print_image(clamp(brightness(image)))