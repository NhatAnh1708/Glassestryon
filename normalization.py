import cv2 as cv


img_path = 'dataset/face.png'


img = cv.imread(img_path)
img_new = cv.resize(img,(144,144))
cv.imwrite('dataset/visual.png',img_new)
print(img_new.shape)
