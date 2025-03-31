import cv2 as cv
import sys

img=cv.imread('/Users/jipyeongseon/Desktop/대학원/2025년 1학기/영상처리 실제/workspace/2주차/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()