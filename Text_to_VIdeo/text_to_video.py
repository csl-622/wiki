import cv2
import os
import time

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

fileName = "output.txt"
fp = open(fileName,"r")
i = 0
for line in fp:
	font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf",25)
	text_size = font.getsize(line)
	button_size = (500, 500)
	img=Image.new("RGBA", button_size,(0,0,0))
	draw = ImageDraw.Draw(img)
	draw.text((0, 0),line+ "\n" + "Hello",(255,255,0),font=font)
	draw = ImageDraw.Draw(img)
	imgName = "images/test" + str(i) + ".png"
	img.save(imgName)
	i+=1


#Making the video.
image_folder = 'images'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
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
