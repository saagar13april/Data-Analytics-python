import cv2

#create a Videocapture object
cam = cv2.VideoCapture(0)

while cam.isOpened():
    status , image = cam.read()
    # gray 
    gray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    #sacle to 50%

    img_scaled =cv2.resize(image ,None ,fx=0.5 ,fy=0.5)

    cv2.imshow('scaled' ,img_scaled)
    cv2.imshow('b/w' , gray)
    cv2.imshow('Live' ,image)
    if cv2.waitKey(1) == ord('q'):
        print('You presses q Key')
        break
cam.release()
cv2.destroyAllWindows()