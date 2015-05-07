import cv2
import numpy as np

class crop:
  #  drawing = False
  #  img = cv2.imread('roi.jpg')
  #  ix,iy = -1,-1
#    list = np.array([[]])
    def __init__(self, d=False, i=None,l =np.array([[]]), ix1=-1,iy1=-1):
        global drawing,img,list,ix,iy
        self.drawing = d
        self.img =i
        self.list = l
        self.ix =ix1
        self.iy=iy1
    def get_img(self):
        return self.img
    def get_list(self):
        return self.list
    def draw_circle(self,event,x,y,flags,param):
        #global ix,iy,drawing,list,img
        ix = self.ix
        iy = self.iy
        list = self.list
        img = self.img
        drawing = self.drawing
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
        self.drawing = drawing
        self.img =img
        self.list = list
        self.ix =ix
        self.iy=iy

    def cropping(self,list,img):
        mask = img
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
       # cv2.imshow('image',blank)
      #  cv2.waitKey(0)
        leftmost = list[list[:,0].argmin()][0]
        rightmost = list[list[:,0].argmax()][0]
        topmost = list[list[:,1].argmin()][1]
        bottommost = list[list[:,1].argmax()][1]

        x =leftmost
        y=topmost
        w=rightmost-leftmost
        h=bottommost-topmost

        cloth = np.zeros((h+100,w+100,3), np.uint8)
        for i in range(0,w+100):
            for j in range(0,h+100):
                cloth[j,i] =[255,255,255]

        for i in range(x,w+x):
            for j in range(y,y+h):
                cloth[j-y+50,i-x+50] =blank[j,i]
        return cloth

 #   cv2.namedWindow('image')
 #   cv2.setMouseCallback('image',draw_circle)

 #   while(1):
  #      img = get_img()
  #      cv2.imshow('image',img)
  #      k = cv2.waitKey(1) & 0xFF
  #      if k == ord('w'):
  #          break

#    cv2.destroyAllWindows()
#    cloth = cropping(list,img)
#    cv2.imshow('image',cloth)
#    cv2.waitKey(0)