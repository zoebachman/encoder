#adding W option

from PIL import Image

def get_pixels(image):
  im = Image.open(image)
  return list(im.getdata())



def encode(image):
  all_pixels = get_pixels("plain_heart.jpg")
  # len(all_pixels) = 14470

  count = 1
  #count_list = []


  prev_pixel = ''
  firsttimethough = True



  for pixel in all_pixels: 

  if all_pixels[z] == "B":
  	b_count = b_count + 1 #add 1 to count to start...maybe adding too much? maybe this is how we isolate the 1s...
  	#check to see if next one is also B
  	if all_pixels[(z+1)] == "B":
  		#print("2B") 
  		b_count = b_count + 1 #increment count by 1
  	elif all_pixels[(z+1)] == "W": #but I think the [z:z+1] will be helpful somewhere
  		# count_list.append(str(count) + "B")
  		print(str(b_count) + "B")
  		b_count = 0 #reset count to 0
  	# else:
  	# 	print ("B")

  elif all_pixels[z] == "W":
  	w_count = w_count + 1 # add 1 to count to start
  	#check to see if next one is also W
  	if all_pixels[(z+1)] == "W":
  		w_count = w_count + 1 #increment count by 1
  	elif all_pixels[(z+1)] == "B":
  		print(str(w_count) + "W")
  		w_count = 0 #reset count to 0
  	# else:
  	# 	print("W")
    #print (z)
    #print(z+1) #position one over
    #print(all_pixels[z:(z+1)])

    #list comprehension
# for i in [i for i, x in enumerate(all_pixels) if x == "W"]:
# 	print (i) #printing position in list


#next steps: put them into one long list and convert back into a string
# try and get them as a tuple: print count and letter separately
#BONUS:minimize characters by only having a letter that's isolated not have a number next to it 


#set previous letter to an empty string, but look forward and then back 
#varaible previous letter = ""
