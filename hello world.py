
import cv2

vid = cv2.VideoCapture(0)

a=1

while True:
    a+=1
    check, frame = vid.read()
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    vid2=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey", vid2)
    vid3=cv2.flip(frame, 1)
    cv2.imshow("Flip", vid3)
    if key == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
print(a)