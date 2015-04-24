import cv2
import numpy as np

drawing = False
enclosed = False
img = cv2.imread('roi.jpg')
ix,iy = -1,-1
list = np.array([[]])
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,enclosed,list
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        list = np.array([[ix,iy]])

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img,(ix,iy),(x,y),(0,255,0),1 , 8 , 0)
            ix = x
            iy = y
            point = [[x,y]]
            list = np.append(list,point,axis=0)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img,(ix,iy),(x,y),(0,255,0),1 , 8 , 0)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('w'):
        break

cv2.destroyAllWindows()
mask = cv2.imread('roi.jpg')
width, height = mask.shape[:2]
blank = np.zeros((width,height,3), np.uint8)
for i in range(0,width):
    for j in range(0,height):
        blank[i,j] =[255,255,255]


alist =[]
alist.append(list)
cv2.drawContours(blank, alist, 0,  (0,255,0), -1)
for i in range(0,width):
    for j in range(0,height):
        if blank[i,j,0] ==0:
            blank[i,j] =mask[i,j]
cv2.imshow('image',blank)
cv2.waitKey(0)
leftmost = list[list[:,0].argmin()][0]
rightmost = list[list[:,0].argmax()][0]
topmost = list[list[:,1].argmin()][1]
bottommost = list[list[:,1].argmax()][1]

x =leftmost
y=topmost
w=rightmost-leftmost
h=bottommost-topmost

cloth = np.zeros((h,w,3), np.uint8)
for i in range(0,w):
    for j in range(0,h):
        cloth[j,i] =[255,255,255]

for i in range(x,w+x):
    for j in range(y,y+h):
        cloth[j-y,i-x] =blank[j,i]
cv2.imshow('image',cloth)
cv2.waitKey(0)
cv2.imwrite("cloth.jpg",cloth)