from PIL import Image
im = Image.open("plain_heart.jpg")


px = list(im.getdata())

white_pixels = []
black_pixels = []

#print(px) prints as a list


#px = im.load()
for i in px:
	if i == (0,0,0):
		white_pixels.append(i)
	elif i == (255, 255, 255):
		black_pixels.append(i)

print (len(white_pixels))
print (len(black_pixels))

	#print(i) #prints one by one
#im.show()

#print(im.format, im.size, im.mode)

#print(im.point())
# r, g, b, a = im.split()
# print (r, g, b, a)

#im = Image.merge("RGBA", (a, b, g, r))

