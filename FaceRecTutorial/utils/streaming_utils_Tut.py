import cv2

def getStream(portNum = 0):
    cap = cv2.VideoCapture(portNum)
    if not cap or not cap.isOpened():
        return None
    return cap

