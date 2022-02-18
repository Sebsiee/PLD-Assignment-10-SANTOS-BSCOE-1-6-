import cv2
import datetime

cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    a, img = cam.read()
    data, one, a = detector.detectAndDecode(img)
    if data:
        b = data 
        break
    cv2.imshow("QR Code Scanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

with open("Data.txt", mode='a') as file:
    file.write('Data: %s, Recorded at %s.\n' % (data, datetime.datetime.now()))
    file.close()

print(data)