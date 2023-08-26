import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(60,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Mercury",(120,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Venus",(180,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Earth",(260,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Mars",(350,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Jupiter",(490,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Saturn",(700,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Uranus",(900,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.putText(img,"Neptune",(1100,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(130,200,140))
cv2.imshow("Output",img)

cv2.waitKey(0)
