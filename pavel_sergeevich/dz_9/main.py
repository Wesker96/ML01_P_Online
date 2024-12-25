import cv2
import numpy as np


path2video = "data/video.mp4"

vrd = cv2.VideoCapture(path2video)
vwr = cv2.VideoWriter()

ret, frame = vrd.read()

print(ret)

cv2.imshow("dwd", frame)
cv2.waitKey(0)



print(type(vrd))
print(type(vwr))

print(vrd.get(cv2.CAP_PROP_FRAME_WIDTH))
print(vrd.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(vrd.get(cv2.CAP_PROP_FPS))
print(vrd.get(cv2.CAP_PROP_FRAME_COUNT))



cv2.destroyAllWindows()
