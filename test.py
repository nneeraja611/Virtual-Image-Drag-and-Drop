import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3,1288)  #size of the video
cap.set(4,720)

detector = HandDetector(detectionCon=0.65)

img1=cv2.imread("ImagesJPG/1.jpg")

ox,oy=200,200     #origin x and y
#just change this number to change the location of the image

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands, img=detector.findHands(img,flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        # Check if clicked
        
        length= detector.findDistance(lmList[8],lmList[12],img)
        #finding the distance btw the tip of index and middle finger
        print(length)
        if length<60:
            cursor=lmList[8]

            if ox<cursor[0]<ox+w and oy<cursor[1]<oy+h:  #to check if the index finger is near the image
                ox,oy=cursor[0]-w//2,cursor[1]-h//2  #to make the index finger point to the center of the image
                pass
            
    h,w, _ =img1.shape    #size of the image(height,width)
    img[oy:oy + h, ox:ox + w]=img1   #calculating the location of the image


    cv2.imshow("Image",img)
    cv2.waitKey(1)