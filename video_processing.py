import cv2

cascase_path = 'haarcascade_fullbody.xml'
classifier = cv2.CascadeClassifier(cascase_path)
path = r'C:\Users\ZAID\Videos\u4.exe\vid.mp4' # 0 for webcam, path to video file
video = cv2.VideoCapture(path)
while True:
    status, image = video.read()
    if not status:
        print('Could not read frame')
        break
    # logic
    image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
    detection = classifier.detectMultiScale(image,
                                            scaleFactor=1,
                                            minNeighbors=3,
                                            minSize=(20, 20)) 
    if len(detection) > 0:
        print(f'Found {len(detection)} people')
        for (x, y, w, h) in detection:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('video', image)
    if cv2.waitKey(1) == ord('q'): # if q key is pressed then break
        break
video.release()         # release video capture object
cv2.destroyAllWindows() # close all windows