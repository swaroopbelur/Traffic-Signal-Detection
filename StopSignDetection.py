import cv2
import numpy as np

SS_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')
SpS_cascade = cv2.CascadeClassifier('lbpCascade.xml')

cap = cv2.VideoCapture(0)
i = 0
j = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    SSs = SS_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in SSs:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print "Dimensions are(xywh): " + str(x) + str(y) + str(w) + str(h)
        print "Stop Sign Detected " + str(i)
	i+=1

    SpSs = SpS_cascade.detectMultiScale(gray, 1.3, 5)
    for(a,b,c,d) in SpSs:
        cv2.rectangle(img, (a,b), (a+c, b+d), (0,255,0),2)
        roi_gray = gray[b:b+d, a:a+c]
        roi_color = img[b:b+d, a:a+c]
        print "Dimensions are(xywh): " + str(a) + str(b) + str(c) + str(d)
        print "Speed Sign Detected " + str(j)
    	j+=1

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows();
