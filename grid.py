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
    return value
    
def print_image(image):
    for row in image:
        print(" ".join(f"{pixel:3}" for pixel in row))

def invert(image):
    new_image= create_image(get_width(image), get_height(image))  
    for row in range(get_height(image)):
     for col in range(get_width(image)):
        old_pixel=get_pixel(image,row,col)
        set_pixel(new_image, row, col, 255-old_pixel)  
    return new_image       

def brightness(image,amount):
    new_image=create_image(get_width(image), get_height(image))
    for row in range(get_height(image)):
         for col in range(get_width(image)):
            old_pixel=get_pixel(image,row,col)
            set_pixel(new_image, row, col, clamp(amount+old_pixel))  
    return (new_image) 

def img_threshold(image, threshold):
    
    new_image=create_image(get_width(image), get_height(image))
    for row in range(get_height(image)):
        for col in range(get_width(image)):
            old_pixel=get_pixel(image,row,col)
            set_pixel(new_image,row,col, 255 if old_pixel>=threshold else 0)
    return(new_image)  

def flip_horizontal(image):
   new_image=create_image(get_width(image), get_height(image)) 
   for row in range(get_height(image)):
      for col in range(get_width(image)):
          old_pixel=get_pixel(image,row, get_width(image)-1-col)
          set_pixel(new_image,row,col,old_pixel)
   return(new_image)       

def flip_vertical(image):
    new_image=create_image(get_width(image), get_height(image))
    for row in range(get_height(image)):
        for col in range(get_width(image)):
            old_pixel=get_pixel(image,get_height(image)-1-row,col)
            set_pixel(new_image,row,col,old_pixel)
    return(new_image)      

def flip(image):
    new_image=create_image(get_width(image), get_height(image))
    for row in range(get_height(image)):
        for col in range(get_width(image)):
                old_pixel=get_pixel(image,get_height(image)-1-row,get_width(image)-1-col)
                set_pixel(new_image,row,col,old_pixel)
    return(new_image)


width = int(input("Enter width:"))
height = int(input("Enter height: "))
image = create_image(width, height)
threshold=int(input("enter threshold value:"))
amount = int(input("Enter the amount you want brightness to be increased by (negative decrese in brightness):"))

for row in range(get_height(image)):
    for col in range(get_width(image)):
        pixel=int(input("Enter pixel : "))
        set_pixel(image, row, col, pixel)
        

print_image(image)
print_image(invert(image))
print_image(brightness(image,amount))
print_image(img_threshold(image,threshold))
print_image(flip_horizontal(image))
print_image(flip_vertical(image))
print_image(flip(image))