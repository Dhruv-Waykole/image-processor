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

def crop(image, top, left, new_height, new_width):
    if top < 0 or left < 0 or new_height <= 0 or new_width <= 0:
        raise ValueError("Values must be positive (top and left can be 0)")
    if top + new_height > get_height(image) or left + new_width > get_width(image):
        raise ValueError("Crop area goes outside the image")
    
    new_image=create_image(new_width, new_height)
    for row in range(new_height):
        for col in range(new_width):
            old=get_pixel(image,top+row,left+col)
            set_pixel(new_image,row,col,old)
    return (new_image) 

def clamp_blur(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

def get_pixel_clamped(image, row, col):
    row = clamp_blur(row, 0, get_height(image) - 1)
    col = clamp_blur(col, 0, get_width(image) - 1)
    return image[row][col]

def create_kernel(image, kernel):
    h = get_height(image)
    w = get_width(image)
    kh = len(kernel)
    kw = len(kernel[0])
    offset_r = kh // 2
    offset_c = kw // 2

    divisor = sum(sum(k_row) for k_row in kernel)
    if divisor == 0:
        divisor = 1

    new_image = create_image(w, h)

    for row in range(h):
        for col in range(w):
            total = 0
            for kr in range(kh):
                for kc in range(kw):
                    old_pixel = get_pixel_clamped(image, row + kr - offset_r, col + kc - offset_c)
                    total += old_pixel * kernel[kr][kc]
            set_pixel(new_image, row, col, clamp(round(total / divisor)))

    return new_image



blur_kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]



