import cv2       #pip install opencv-python
from pyzbar.pyzbar import decode        #pip install pyzbar
import time

cam = cv2.VideoCapture(0)  


#dimetions of the frame the camera will appear in

cam.set(5, 640)
cam.set(6, 480)

#getting the permissoin to open the camera
#The camera is False by defualt

camera = True

#loop to capture the qr code

while camera == True:
    success, frame = cam.read()

    if success:
        for barcode in decode(frame):
            print(barcode.type)
            print(barcode.data.decode("utf-8"))
            time.sleep(6)

        cv2.imshow("Scanner", frame)
        cv2.waitKey(3)

#expected error

    else:
        print("Error: Frame not read from camera.")
        break



cam.release()
cv2.destroyAllWindows()
