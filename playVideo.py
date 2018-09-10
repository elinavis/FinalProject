import cv2
import time
import tkMessageBox

time_slot = 5
cap = {}

def startVideo(videoPath):
    global cap

    if cap and cap.isOpened and cap.isOpened():
        return

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(videoPath)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

def showVideo():
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

def playVideo():


    # Read until video is completed
    t_end = time.time() + time_slot
    res = False

    while (cap.isOpened() and  time.time() < t_end):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:

            res = True
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            # break
            return res

    return True



def endOfVideo():
    # When everything done, release the video capture object
    cap.release()

def destroy():

    # Closes all the frames
    cv2.destroyAllWindows()