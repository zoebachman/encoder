#take a string as input and set it to variable 'string'
#look through each character of string and make an evaluation
#look at character next to it, if character is the same, add it to a list
#option 1:

#if same, append to list...somehow evaluate list using len to get list length

#if different, assign character a 1[char name] and append to new string


#option 2:
#just letter and append to new string

#option 3: list comprehension??



#string = input
#parse input so there are commas? [should you keep similar ones together?]

W = "W"
B = "B"

X = 15
new_string = [W,W,B,B,B,W,W,W,W,B,B,B]

for i in new_string:
	print i
print len(new_string)

for i in range(1,X):
	print new_string[0:(len(new_string)-1)]

	#print j
	# if [i] == [i++]: #how to define the position after i?
	# 	#increase count >> where is this being stored?
	# else:
	# 	new_string.append(i)