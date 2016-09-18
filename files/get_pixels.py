
from PIL import Image

def get_pixels(image):
	im = Image.open(image)
	return list(im.getdata())
