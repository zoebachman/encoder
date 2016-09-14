#cleaned up code
#printing amounts of white and black pixels

from PIL import Image
im = Image.open("plain_heart.jpg")


px = list(im.getdata())

white_pixels = []
black_pixels = []


for i in px:
	if i == (0,0,0):
		white_pixels.append(i)
	elif i == (255, 255, 255):
		black_pixels.append(i)

print (len(white_pixels))
print (len(black_pixels))


