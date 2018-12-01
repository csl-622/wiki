import cv
resim = cv.LoadImage('image.jpg')
capture = cv.CaptureFromFile('video.avi')
while(1):
    frame = cv.QueryFrame(capture)
    cv.SetImageROI(frame,(100,100,resim.width,resim.height))
    cv.Add(frame,resim,frame)
    cv.ResetImageROI(frame)
    cv.ShowImage('frame',frame)
    if cv.WaitKey(33)==27:
        break
