import numpy as np    #pip install numpy
import cv2            #pip install opencv-python

img = cv2.imread('shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, imgBlack = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(255-imgBlack, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE ) #255-imgBlack invertiert das Bild

cv2.imshow("original img", img)
cv2.imshow("imgBlack", imgBlack)



""" alle Konturen der Formen im Bild sind in "contours" abgespeichert.
    Mit der "for" Schlaufe wird durch alle Formen in "contours" durchgegangen.
"""
for contour in contours:

    # mache aus der Kontur approximierte Poligonlinien
    schwellwert = 0.03 * cv2.arcLength(contour, True)
    linien_umrisse = cv2.approxPolyDP(contour, schwellwert, True)
    
    # zeichne die linien_umrisse in das original Bild
    ColorBlack = (0,0,0)
    Linien_dicke = 2
    cv2.drawContours(img, [linien_umrisse], 0, ColorBlack, Linien_dicke)

    x = linien_umrisse.ravel()[0]
    y = linien_umrisse.ravel()[1] - 5

    if len(linien_umrisse) == 3:
        cv2.putText(img, "Dreieck", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)
    elif len(linien_umrisse) == 4:
        x1 ,y1, w, h = cv2.boundingRect(linien_umrisse)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "Quadrat", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)
        else:
          cv2.putText(img, "Rechteck", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)
    elif len(linien_umrisse) == 5:
        cv2.putText(img, "Fünfeck", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)
    elif len(linien_umrisse) == 10:
        cv2.putText(img, "Stern", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)
    else:
        cv2.putText(img, "Kreis", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ColorBlack)


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()