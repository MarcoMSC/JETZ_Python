import numpy as np    #pip install numpy
import cv2            #pip install opencv-python

img = cv2.imread('shape.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, imgBlack = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(255-imgBlack, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE ) #255-imgBlack invertiert das Bild


# mache aus der Kontur approximierte Poligonlinien
schwellwert = 0.03 * cv2.arcLength(contours[0], True)
linien_umrisse = cv2.approxPolyDP(contours[0], schwellwert, True)

if len(linien_umrisse) == 3:
    print("Dreieck")
elif len(linien_umrisse) == 4:
    print("Rechteck")
elif len(linien_umrisse) == 5:
    print("Fünfeck")
elif len(linien_umrisse) == 10:
    print("Stern")
else:
    print("Kreis")


cv2.imshow("original img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()