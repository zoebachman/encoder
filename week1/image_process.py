#cleaned up code
#printing amounts of white and black pixels

from PIL import Image
im = Image.open("plain_heart.jpg")


px = list(im.getdata())

white_pixels = []
black_pixels = []

all_pixels = []


for i in px:
	if i == (0,0,0):
		all_pixels.append("W")
	elif i == (255, 255, 255):
		all_pixels.append("B")

#print(all_pixels)

#list comprehension
# for i in [i for i, x in enumerate(all_pixels) if x == "W"]:
# 	print (i) #printing position in list

for j in all_pixels:
	print all_pixels.index(j)
	#print (all_pixels[0]) #getting stuck on relating position
	#print (all_pixels[0:len(all_pixels - j)])


