import sys
import cv2
import numpy as np
from random import randint

trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
    if trackerType == trackerTypes[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == trackerTypes[1]:
        tracker = cv2.TrackerMIL_create()
    elif trackerType == trackerTypes[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == trackerTypes[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == trackerTypes[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == trackerTypes[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif trackerType == trackerTypes[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == trackerTypes[7]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None
        print('Incorrect tracker name')
        print('Available trackers are:')
        for t in trackerTypes:
           print(t)

    return tracker

def get_cars(tfnet,frame):
    result = tfnet.return_predict(frame)
    return result


def start_tracking(path, results, tfnet):

    cap = cv2.VideoCapture(path)
    success, frame = cap.read()
    frame = np.asarray(frame)

    if not success:
        print('Failed to read video')
        sys.exit(1)

    bboxes = []
    colors = []




    for b in results:
        bboxes.append(b)
        colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))


    print('Selected bounding boxes {}'.format(bboxes))
    trackerType = "CSRT"


    multiTracker = cv2.MultiTracker_create()


    for bbox in bboxes:
        multiTracker.add(createTrackerByName(trackerType), frame, bbox)

    counter = 0
    while cap.isOpened():
        counter = counter + 1

        success, frame = cap.read()
        if not success:
            break

        if counter % 10 == 0:
            f = np.asarray(frame)
            temp = get_cars(tfnet,f)
            print (get_vehical_boxes(temp))


        success, boxes = multiTracker.update(frame)


        for i, newbox in enumerate(boxes):
            p1 = (int(newbox[0]), int(newbox[1]))
            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, p1, p2, colors[i], 2, 1)


        cv2.imshow('MultiTracker', frame)


        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
            break



def get_vehical_boxes(result):
        boxes = list()
        for r in result:
            if r['label'] == 'car':
              topleft_x = r['topleft']['x']
              topleft_y = r['topleft']['y']
              bottomright_x = r['bottomright']['x']
              bottomright_y = r['bottomright']['y']
              tup = (topleft_x,topleft_y,bottomright_x - topleft_x, bottomright_y - topleft_y)
              boxes.append(tup)

        return boxes
