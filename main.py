import os
from PIL import Image, ImageSequence
from resizeimage import resizeimage

import svgutils

def thumbnails(frames):
	size = 150, 150
	for frame in frames:
		thumbnail = frame.copy()
		thumbnail.thumbnail(size, Image.ANTIALIAS)
		yield thumbnail

for filename in os.listdir(os.getcwd() + "/sample-images"):
	final = filename.split(".")[1]
	if final == "jpg" or final == "png":
		with open(os.getcwd() + "/sample-images/" + filename, 'r+b') as f:
			with Image.open(f) as image:
				cover = resizeimage.resize_cover(image, [150, 150])
				cover.save(os.getcwd() + "/sample-images/" + filename.split(".")[0] + '_copy.' + final, image.format)

	elif final == "gif":
		with open(os.getcwd() + "/sample-images/" + filename, 'r+b') as f:
			with Image.open(f) as image:
				frames = ImageSequence.Iterator(image)
		  

				frames = thumbnails(frames)
				om = next(frames) # Handle first frame separately
				om.info = image.info # Copy sequence info
				om.save(os.getcwd() + "/sample-images/" + filename.split(".")[0] + '_copy.' + final, save_all=True, append_images=list(frames))

	elif final == "svg":
		originalSVG = svgutils.compose.SVG(os.getcwd() + "/sample-images/" + filename)
		figure = svgutils.compose.Figure(150, 150, originalSVG)
		figure.save(os.getcwd() + "/sample-images/" + filename.split(".")[0] + '_copy.' + final)

