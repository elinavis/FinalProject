from Tkinter import *
import json
import tkMessageBox
from playVideo import *

video_time = 0
results = {}

def onSubmit():
    global video_time

    selected_subject = subject.get()

    if not selected_subject:
        tkMessageBox.showerror("no subject", "select a subject to continue")
        return

    if selected_subject not in results:
        results[selected_subject] = []
        playVideo()
        return

    var_6_res = []
    for item in var_6:
        if item.get():
            var_6_res.append(item.ui_value)

    results[selected_subject].append({
       'turn': turn.get(),
       'start_time' : video_time,
       'end_time' : video_time + time_slot,
       'Gaze direction': var_1.get(),
       'Body orientation':  var_2.get(),
       'Body posture':  var_3.get(),
       'Head orientation':  var_4.get(),
       'Head movement':  var_5.get(),
       'Gestures':  var_6_res,
       'Emotions':  var_7.get(),
       'Expressions':  var_8.get(),
    })

    video_time += time_slot
    playVideo()

##################################################################################################
##### build UI###############
##################################################################################################
root = Tk()

Label(root, text = "Round #", font='Helvetica 11 bold').grid(row =1, column = 1)
round = StringVar()
OptionMenu(root, round, 0, 1).grid(row =1, column = 2)

Label(root, text = "Participant/subject:", font='Helvetica 11 bold').grid(row =2, column = 1)
subject = StringVar()
OptionMenu(root, subject,'A', 'B', 'C', 'D').grid(row =2, column = 2)

Label(root, text = "The turn of participant:", font='Helvetica 11 bold').grid(row =3, column = 1)
turn = StringVar()
OptionMenu(root, turn,'A', 'B', 'C', 'D').grid(row =3, column = 2)




ui_data_structure = {}
###### Gaze direction section  #######
ui_data_structure["Gaze direction"] = ["Left", "Right", "Straight", "Up", "Down", "Aversion"]
Label(root, text = "Gaze direction", font='Helvetica 11 bold').grid(row =5)
var_1 = StringVar()

for idx, val in enumerate(ui_data_structure["Gaze direction"]):
    Radiobutton(root, text=val, variable=var_1, value=val).grid(sticky = W, row =6, column =idx)


###### Body orientation section  #######
ui_data_structure["Body orientation"] = ["Left", "Right", "Straight"]
Label(root, text = "Body orientation", font='Helvetica 11 bold').grid(row =7)
var_2 = StringVar()

for idx, val in enumerate(ui_data_structure["Body orientation"]):
    Radiobutton(root, text=val, variable=var_2, value=val).grid(sticky = W,row=8, column=idx)


###### Body posture section  #######
ui_data_structure["Body posture"] = ["Leaning Front", "Neutral", "Leaning Back"]
Label(root, text = "Body posture", font='Helvetica 11 bold').grid(row =9)
var_3 = StringVar()

for idx, val in enumerate(ui_data_structure["Body posture"]):
    Radiobutton(root, text=val, variable=var_3, value=val).grid(sticky = W,row=10, column=idx)

###### Head orientation section  #######
ui_data_structure["Head orientation"] = ["Left", "Right", "Straight"]
Label(root, text = "Head orientation", font='Helvetica 11 bold').grid(row =11)
var_4 = StringVar()

for idx, val in enumerate(ui_data_structure["Head orientation"]):
    Radiobutton(root, text=val, variable=var_4, value=val).grid(sticky = W,row=12, column=idx)


###### Head movement section  #######
ui_data_structure["Head movement"] = ["Nodding", "Head Shaking", "tilting"]
Label(root, text = "Head movement", font='Helvetica 11 bold').grid(row =13)
var_5 = StringVar()

for idx, val in enumerate(ui_data_structure["Head movement"]):
    Radiobutton(root, text=val, variable=var_5, value=val).grid(sticky = W,row=14, column=idx)


###### Gestures section  #######
ui_data_structure["Gestures"] = ["Hand palms together", "separated", "head leaning on hand", "hands touching face/body"]
Label(root, text = "Gestures", font='Helvetica 11 bold').grid(row =15)
var_6 = []

for idx, val in enumerate(ui_data_structure["Gestures"]):
    var= IntVar()
    var_6.append(var)
    var.set(0)
    setattr(var, "ui_value", val)
    Checkbutton(root, text=val, variable=var ).grid(sticky = W,row=16, column=idx)


###### Emotions section  #######
ui_data_structure["Emotions"] = ["fear", "sadness", "happiness", "anger", "disgust", "surprise"]
Label(root, text = "Emotions", font='Helvetica 11 bold').grid(row =17)
var_7 = StringVar()

for idx, val in enumerate(ui_data_structure["Emotions"]):
    Radiobutton(root, text=val, variable=var_7, value=val).grid(sticky = W,row=18, column=idx)


###### Expressions section  #######
ui_data_structure["Expressions"] = ["Smiling", "Eyebrows raised/lowered", "Grimase"]
Label(root, text = "Expressions", font='Helvetica 11 bold').grid(row =19)
var_8 = StringVar()

for idx, val in enumerate(ui_data_structure["Expressions"]):
    Radiobutton(root, text=val, variable=var_8, value=val).grid(sticky = W,row=20, column=idx)



Button(root, text="Play", command = onSubmit).grid(row =21)

##################################################################################################


startVideo()
root.mainloop()
endOfVideo()
### at the end, print the file
with open('data.js', 'w') as outfile:
    json.dump(results, outfile)