import cv2
import numpy as np

theta = 18 * np.pi / 180
rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]], np.float32)
image = np.full((500, 500, 3), 0, np.uint8)
pts1 = np.array([(0, -60), (70, 50),
                 (-70, 50)], np.float32)
pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)


def move1(pts):
    for i in range(3):
        pts[i][0] = pts[i][0] + 250
        pts[i][1] = pts[i][1] + 250
    return pts

def move2(pts):
    for i in range(3):
        pts[i][0] = pts[i][0] - 250
        pts[i][1] = pts[i][1] - 250
    return pts

move1(pts1)
cv2.polylines(image, [np.int32(pts1)], True, (255, 255, 255), 2)
move2(pts1)


for _ in range(30):
    pts2 = move1(pts2)
    cv2.polylines(image, [np.int32(pts2)], True, (255, 255, 255), 2)
    pts2 = move2(pts2)
    pts2 = cv2.gemm(pts2, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)


cv2.imshow("image", image)
cv2.waitKey(0)
