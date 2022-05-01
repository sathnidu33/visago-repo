# import time
# import cv2
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# ret, frame = cap.read()
# #cap.release()
# cv2.imwrite(frame)
# print(frame.shape)
# frame = cv2.resize(frame, (720, 480))
# cv2.imwrite('img1.png', frame)
#
# time.sleep(3)
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# ret, frame = cap.read()
# cap.release()
# frame = cv2.resize(frame, (720, 480))
# cv2.imwrite('img2.png', frame)
#
# cv2.imshow('frame', frame)

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

for i in range(10):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
print(frame)
