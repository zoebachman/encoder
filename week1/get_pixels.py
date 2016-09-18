
from PIL import Image

def getpixel(image):
	im = Image.open(image)
	px = list(im.getdata())
	return px

print(getpixel("plain_heart_bw.jpg"))