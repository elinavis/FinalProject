from naoqi import ALProxy, ALModule, ALBroker
from Tkinter import *
import time


IP ='192.168.0.100'
PORT=9559

####Initialize the API's
motionProxy = ALProxy("ALMotion",IP ,PORT )
memory = ALProxy("ALMemory", IP, PORT)
managerProxy = ALProxy("ALBehaviorManager", IP, PORT)


# We need this broker to be able to construct
# NAOqi modules and subscribe to other modules
# The broker must stay alive until the program exists
myBroker = ALBroker("myBroker",
                    "0.0.0.0",  # listen to anyone
                    0,  # find a free port and use it
                    IP,  # parent broker IP
                    PORT)  # parent broker port


# param to decide on the hand movement

def move_hands_robot():
    global j

    if(j%2 == 0):
        pMaxSpeedFraction = 0.35
        pNames = ['LShoulderRoll', 'RShoulderRoll']
        pTargetAnglesUp = [1.3265, -1.3265]  # angels to be set for the joints in radians (if more the one - list)
        pTargetAnglesDown = [-0.3142, 0.3142]
        for i in range(0, 3):
            motionProxy.post.angleInterpolationWithSpeed(pNames, pTargetAnglesUp, pMaxSpeedFraction)
            motionProxy.post.angleInterpolationWithSpeed(pNames, pTargetAnglesDown, pMaxSpeedFraction)

    else:
        pNames1 = ['LShoulderPitch', 'RShoulderPitch']
        pMaxSpeedFraction = 0.2
        pTargetAnglesPitch = [-1, -1]
        pTargetAnglesPitchDown = [1.5, 1.5]

        for i in range(0, 3):
            motionProxy.post.angleInterpolationWithSpeed(pNames1, pTargetAnglesPitch, pMaxSpeedFraction)
            motionProxy.post.angleInterpolationWithSpeed(pNames1, pTargetAnglesPitchDown, pMaxSpeedFraction)

    j+=1


def define_next_action(happy_ratio, conc_ratio):
    # according to the Q map from HW2
    if happy_ratio >= 0.7 and conc_ratio >= 0.7:
       return 1
    elif happy_ratio < 0.7 and conc_ratio < 0.7:
        return 1
    elif happy_ratio < 0.7 and conc_ratio >= 0.7:
        return 0
    else:
        return 1



def do_action (happy_ratio, conc_ratio):
    action = define_next_action(happy_ratio, conc_ratio)
    if action == 0:
        # moving body
        managerProxy.post.runBehavior("Stand/Emotions/Positive/Excited_2")
        managerProxy.post.runBehavior("dialog_posture/bhv_stand_up")
    elif action == 1:
        move_hands_robot()



def end_sad_interaction ():
    tts.say("I believe, you don't feel like listening to the story right now.")
    tts.say("Till next time!")
    managerProxy.runBehavior("Stand/Emotions/Neutral/Hello_1")
    managerProxy.runBehavior("dialog_posture/bhv_sit_down")

number_tries= 1
def child_didnt_come():
    global number_tries
    number_tries = number_tries + 1

    if (number_tries == 4):
        return end_sad_interaction()

    #Call the child same as in the start
    if number_tries == 2:
        tts.post.say("Come, please come!")
        managerProxy.runBehavior("Stand/Emotions/Neutral/Hello_1")

    elif number_tries == 3:
        managerProxy.runBehavior("Stand/Emotions/Positive/Happy_1")
        tts.say("It is going to be fun, come join me!")




def start_robot():

    global number_tries
    number_tries = 1
    managerProxy.runBehavior("dialog_posture/bhv_stand_up")

    # managerProxy.runBehavior("dialog_posture/bhv_sit_down")
    managerProxy.runBehavior("Stand/Emotions/Neutral/AskForAttention_1")  # whisle
    # managerProxy.runBehavior("dialog_posture/bhv_stand_up")

    #stand and call child
    managerProxy.runBehavior("Stand/Emotions/Neutral/AskForAttention_2")
    tts.say("Come, I gonna tell you a story!")


def end_story():
    tts.say("I had so much fun with you! I hope you enjoyed the story. Bye Bye")

    managerProxy.runBehavior("Stand/Emotions/Neutral/Hello_1")
    managerProxy.runBehavior("dialog_posture/bhv_sit_down")


