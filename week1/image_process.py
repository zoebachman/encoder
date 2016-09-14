#cleaned up code
#printing amounts of white and black pixels

from PIL import Image
im = Image.open("plain_heart.jpg")


px = list(im.getdata())

# white_pixels = []
# black_pixels = []

all_pixels = []

count = 0

count_list = []


for i in px:
	if i == (0,0,0):
		all_pixels.append("W")
	elif i == (255, 255, 255):
		all_pixels.append("B")

# len(all_pixels) = 14470
print(len(all_pixels))

for z in range(len(all_pixels)): #getting position
  if all_pixels[z] == "B":
  	#check to see if next one is also B
  	if all_pixels[(z+1)] == "B":
  		#print("2B") 
  		count = count + 1 #increment count by 1
  	elif all_pixels[(z+1)] == "W": #but I think the [z:z+1] will be helpful somewhere
  		# count_list.append(str(count) + "B")
  		print(str(count) + "B")
  		count = 0 #reset count to 0
  	else:
  		print ("no")
    #print (z)
    #print(z+1) #position one over
    #print(all_pixels[z:(z+1)])

    #list comprehension
# for i in [i for i, x in enumerate(all_pixels) if x == "W"]:
# 	print (i) #printing position in list


