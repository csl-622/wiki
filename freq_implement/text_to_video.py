import cv2
import os
import time

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def get_video():
	fileName = "output.txt"
	fp = open(fileName,"r")
	i = 0
	images = []
	for line in fp:
		words = [x.strip() for x in line.split(' ')]
		line_text = ""
		curr_len = 0
		for word in words:
			if(curr_len + len(word) > 37):
				curr_len = 0
				line_text = line_text + "\n"
			curr_len+=len(word)+1
			line_text = line_text + word +" " 
		
		font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf",25)
		text_size = font.getsize(line)
		button_size = (500, 500)
		img=Image.new("RGBA", button_size,(0,0,0))
		draw = ImageDraw.Draw(img)
		draw.text((0, 0),line_text,(255,255,0),font=font)
		draw = ImageDraw.Draw(img)
		imgName = "test" + str(i) + ".png"
		images.append(imgName)
		imgName = "images/" + imgName
		img.save(imgName)
		i+=1

	#Making the video.
	image_folder = 'images'
	video_name = 'video.avi'
	frame = cv2.imread(os.path.join(image_folder, images[0]))
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 1, (width,height),1)

	for image in images:
		img = cv2.imread(os.path.join(image_folder, image))
		start_time = time.time()
		fps = 0.05
		while(time.time() - start_time < fps):
		        time.sleep(0.01)
			video.write(img)
			

	cv2.destroyAllWindows()
	video.release()


