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


# for j in all_pixels:
# 	position = all_pixels.index(j) #either 0 or 583?
	#print (all_pixels[0]) #getting stuck on relating position
	#print (all_pixels[0:len(all_pixels - j)])

for z in range(len(all_pixels)): #getting position
  if all_pixels[z] == "B":
  	#check to see if next one is also B
  	if all_pixels[(z+1)] == "B":
  		print("2B")
  	# elif all_pixels[z:(z+1)] == "W":
  	# 	print("BW")
  	# else:
  	# 	print ("no")
    #print (z)
    #print(z+1) #position one over
    #print(all_pixels[z:(z+1)])

    #list comprehension
# for i in [i for i, x in enumerate(all_pixels) if x == "W"]:
# 	print (i) #printing position in list


