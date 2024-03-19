import cv2

def cv_work_with_img():
    img = cv2.imread('test.jpeg')
    # print(img.shape)
    img = cv2.resize(img, (500, 500))
    cv2.imshow('Result', img)
    cv2.waitKey(0)

def cv_work_with_face_detection():
    face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)#('video.mp4')

    while True:
        success, frame = cap.read() #0,1 - to get frame, frame - set of images

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert color bgr to gray
        faces = face_cascades.detectMultiScale(img_gray)

        for (x, y, w, h) in faces: # x,y - start point for rectangle; w,h - rectangle weight and height
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xff == ord('q'): # exit by 'q' key
            break