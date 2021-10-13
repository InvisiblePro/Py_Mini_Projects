import cv2
import random
import time


cap = cv2.VideoCapture(0)
count = 0
b = random.randint(1, 10000)
while True:
    ret, img = cap.read()
    cv2.imshow("Camera", img)
    if not ret:
        break
    k = cv2.waitKey(50)
    if k % 256 == 27:
        print("Closing Camera")
        break

    if k % 256 == 32:
        time.sleep(1)
        file = r'Pictures\img' + str(count) + str(b) + '.jpeg'
        cv2.imwrite(file, img)
        count += 1
cap.release()
cv2.destroyAllWindows()
