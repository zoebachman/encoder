from PIL import Image
from get_pixels import get_pixels


def image_encode(image):
    all_pixels = get_pixels(image)
    count = 1 #int


    prev_pixel = '' #tuple?
    firsttimethough = True
    
    result = []
    #each_pixel_count #empty string

    for pixel in all_pixels: 


        if (pixel == prev_pixel):
            count += 1 #increase count by one


        elif (pixel != prev_pixel):

            if firsttimethough == False: #this condition only applies to first time through
                #same as .append - adding to results list

                if count == 1:
                    result += "(" + str(prev_pixel) + ")" + ", " 

                elif count > 1:
                    result += "(" + str(count) + ", " + " "
                    result += str(prev_pixel) + ")" + ", "

                count = 1 #reset count

            firsttimethough = False

        prev_pixel = pixel #change current pixel to previous pixel


    result += "(" + str(count) + ", " + " " #now that we've gone all the way through, printing count and pixel
    result += str(prev_pixel) + ")"


    return ''.join(result)
    


if __name__ == "__main__": #calling the image_encode function
    print(image_encode("heart_12px.png")) #how to make this modular


