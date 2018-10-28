import cv2
import os

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf",25)
img=Image.new("RGBA", (200,200),(120,20,20))
draw = ImageDraw.Draw(img)
draw.text((0, 0),"This is a test",(255,255,0),font=font)
draw = ImageDraw.Draw(img)
img.save("images/test.png")

image_folder = 'images'


video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 1/10, (width,height),1)

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
