import cv2
import numpy as np


pt = (-1, -1)
title = "window"
image = cv2.imread("./images.jpeg")


def onMouse(event, x, y, flags, params):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x, y), (0, 0, 255), 2)
            cv2.putText(image, "cat", pt, cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.imshow(title, image)

            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, pt, radius, (0, 0, 255), 2, 5)
            cv2.imshow(title, image)
            pt = (-1, -1)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)


while True:
    key = cv2.waitKeyEx(100)
    if key == 27:
        break

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
