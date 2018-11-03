import numpy as np
import os
import cv2
import dlib
import math
from omega import Point, dbPoints
scriptDir = os.path.dirname(os.path.realpath('__file__'))
#imagePath = os.path.join(scriptDir,"wface/img000.png")

for i in range(0,52):
    if i < 10:
        imagePath = "img00" + str(i) + ".png"
    else:
        imagePath = "img0" + str(i) + ".png"
    print(imagePath)
    cascPath = "haarcascade_frontalface_default.xml"
    print(imagePath)
    PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

    JAWLINE_POINTS = list(range(0, 17))
    RIGHT_EYEBROW_POINTS = list(range(17, 22))
    LEFT_EYEBROW_POINTS = list(range(22, 27))
    NOSE_POINTS = list(range(27, 36))
    RIGHT_EYE_POINTS = list(range(36, 42))
    LEFT_EYE_POINTS = list(range(42, 48))
    MOUTH_OUTLINE_POINTS = list(range(48, 61))
    MOUTH_INNER_POINTS = list(range(61, 68))
    ALL_POINTS = list(range(0,68))
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    pointArray = []
    pointArrayX = []
    pointArrayY = []
    points = []

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))
    maxX = -1
    maxY = -1
    minX = 100000000000
    minY = 100000000000
     # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Converting the OpenCV rectangle coordinates to Dlib rectangle
        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        landmarks = np.matrix([[p.x, p.y] for p in predictor(image, dlib_rect).parts()])
        landmarks_display = landmarks[ALL_POINTS]
        for idx, point in enumerate(landmarks_display):
            print(point)
            print(point.item(0))

            pointArrayX.append(point.item(0))
            print(point.item(1))
            #max X and Y
            if point.item(0) > maxX:
                maxX = point.item(0)
            if point.item(1) > maxY:
                maxY = point.item(1)
            if point.item(0) < minX:
                minX = point.item(0)
            if point.item(1) < minY:
                minY = point.item(1)
            #print(point[1])
            pointArray.append(point)
            pointArrayY.append(point.item(1))
            testPoint = Point()
            testPoint.setPoint(point.item(0),point.item(1))
            points.append(testPoint)
            pos = (point[0, 0], point[0, 1])
            cv2.circle(image, pos, 2, color=(0, 0, 255), thickness=3)

    cv2.imshow("Landmarks found", image)
    print("It's time for the main event")
    cv2.waitKey(0)

    #print(JAWLINE_POINTS)
    #print(points)
    for i in range(len(points)):
        points[i].printPoint()
    print("Time to get swifty in here!\n")
    choice = 'y'

    if(choice == 'y'):
        for i in range(len(points)):
            points[i].swiftyProtocol(minX,minY,maxX,maxY)
            points[i].printPoint()
    print(str(minX) + " " + str(minY))
    print((maxX-minX)^2)
    print(maxY-minY)
    print(math.sqrt(float(maxX^2 + maxY^2)))
    #choice = input("Should we get save to the database?(y/n)\n")
    if(choice == 'y'):
        print("Adding to database")

        #def __init__(self, imgName, points):
        dbPoints(imagePath, points)


    #this should do it.
    print(imagePath)
