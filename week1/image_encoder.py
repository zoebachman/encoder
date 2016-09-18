from PIL import Image

def get_pixels(image):
  im = Image.open(image)
  return list(im.getdata())


def image_encode(image):
    all_pixels = get_pixels(image)
    count = 1


    prev_pixel = ''
    firsttimethough = True
    
    result = []


    for pixel in all_pixels: 


        if (pixel == prev_pixel):
        count += 1 #increase count by one


        elif (pixel != prev_pixel):

            if firsttimethough = False: #this condition only applies to first time through
                result += (str(count)) #same as .append - adding to results list
                result += prev_pixel

                count = 1 #reset count

            firsttimethough = False

        prev_pixel = pixel #change current pixel to previous pixel


    result += str(count) #now that we've gone all the way through, printing count and pixel
    result += prev_pixel 



    return ''.join(result) #turning them all into a string


if __name__ == "__main__": #calling the image_encode function
    print(image_encode("plain_heart.jpg"))





# try and get them as a tuple: print count and letter separately
#BONUS:minimize characters by only having a letter that's isolated not have a number next to it 
