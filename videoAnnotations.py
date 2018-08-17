from Tkinter import *
import tkFileDialog
import json
import tkMessageBox
from playVideo import *


class VideoAnnotations():

    def __init__(self):
        self.video_time = 0
        self.results = {}
        self.root = Tk()
        self.firstView = Frame(self.root)
        self.mainView = Frame(self.root)

        self.video_path_var = StringVar()
        self.exp_number_var = StringVar()
        self.round_var = StringVar()

        self.subject_var = StringVar()
        self.turn_var = StringVar()

        self.gaze_direction_var = StringVar()
        self.body_orientation_var = StringVar()
        self.body_posture_var = StringVar()
        self.head_orientation_var = StringVar()
        self.head_movement_var = StringVar()
        self.gestures_var = []
        self.emotions_var = StringVar()
        self.expressions_var = StringVar()

        self.ui_data_structure = {}
        self.ui_data_structure["Gaze direction"] = ["Left", "Right", "Straight", "Up", "Down", "Aversion"]
        self.ui_data_structure["Body orientation"] = ["Left", "Right", "Straight"]
        self.ui_data_structure["Body posture"] = ["Leaning Front", "Neutral", "Leaning Back"]
        self.ui_data_structure["Head orientation"] = ["Left", "Right", "Straight"]
        self.ui_data_structure["Head movement"] = ["Nodding", "Head Shaking", "tilting"]
        self.ui_data_structure["Gestures"] = ["Hand palms together", "separated", "head leaning on hand", "hands touching face/body"]
        self.ui_data_structure["Emotions"] = ["fear", "sadness", "happiness", "anger", "disgust", "surprise"]
        self.ui_data_structure["Expressions"] = ["Smiling", "Eyebrows raised/lowered", "Grimase"]

        self._createFirstView()
        self._createMainView()

    def start(self):
        self.firstView.grid(row=0, column = 0)
        self.root.mainloop()

    def _goToMainView(self):
        self.firstView.grid_forget()
        self.mainView.grid(row=0, column = 0)
        startVideo(self.video_path_var.get())


    def _createFirstView(self):

        Label(self.firstView, text="Select the video to annotate:").grid(row =0, column = 0)
        Button(self.firstView, text="Browse", command=self._browse_button).grid(row=1, column=3)
        Label(self.firstView, textvariable= self.video_path_var).grid(row=1, column=0)

        Label(self.firstView, text= "exp. number:").grid(row=2, column=0)
        OptionMenu(self.firstView, self.exp_number_var, *range(1,12) ).grid(row=2, column=2)

        Label(self.firstView, text="Round number").grid(row=3, column=0)
        OptionMenu(self.firstView, self.round_var, 0, 1).grid(row=3, column=2)

        Button(self.firstView, text="Submit", command=self._goToMainView).grid(row=4, column=3)


    def _createMainView(self):

        Label(self.mainView, text="Participant that is being watched:").grid(row=1, column=1)
        OptionMenu(self.mainView, self.subject_var, 'A', 'B', 'C', 'D').grid(row=1, column=2)

        Label(self.mainView, text="The turn of participant:").grid(row=2, column=1)
        OptionMenu(self.mainView, self.turn_var, 'A', 'B', 'C', 'D').grid(row=2, column=2)


        ###### Gaze direction section  #######
        Label(self.mainView, text="Gaze direction").grid(row=5)

        for idx, val in enumerate(self.ui_data_structure["Gaze direction"]):
            Radiobutton(self.mainView, text=val, variable=self.gaze_direction_var, value=val).grid(sticky=W, row=6, column=idx)

        ###### Body orientation section  #######
        Label(self.mainView, text="Body orientation").grid(row=7)

        for idx, val in enumerate(self.ui_data_structure["Body orientation"]):
            Radiobutton(self.mainView, text=val, variable=self.body_orientation_var, value=val).grid(sticky=W, row=8, column=idx)

        ###### Body posture section  #######
        Label(self.mainView, text="Body posture").grid(row=9)

        for idx, val in enumerate(self.ui_data_structure["Body posture"]):
            Radiobutton(self.mainView, text=val, variable=self.body_posture_var, value=val).grid(sticky=W, row=10, column=idx)

        ###### Head orientation section  #######
        Label(self.mainView, text="Head orientation").grid(row=11)

        for idx, val in enumerate(self.ui_data_structure["Head orientation"]):
            Radiobutton(self.mainView, text=val, variable=self.head_orientation_var, value=val).grid(sticky=W, row=12, column=idx)

        ###### Head movement section  #######
        Label(self.mainView, text="Head movement").grid(row=13)

        for idx, val in enumerate(self.ui_data_structure["Head movement"]):
            Radiobutton(self.mainView, text=val, variable=self.head_movement_var, value=val).grid(sticky=W, row=14, column=idx)

        ###### Gestures section  #######
        Label(self.mainView, text="Gestures").grid(row=15)

        for idx, val in enumerate(self.ui_data_structure["Gestures"]):
            var = IntVar()
            self.gestures_var.append(var)
            var.set(0)
            setattr(var, "ui_value", val)
            Checkbutton(self.mainView, text=val, variable=var).grid(sticky=W, row=16, column=idx)

        ###### Emotions section  #######
        Label(self.mainView, text="Emotions", font='Helvetica 11 bold').grid(row=17)

        for idx, val in enumerate(self.ui_data_structure["Emotions"]):
            Radiobutton(self.mainView, text=val, variable=self.emotions_var, value=val).grid(sticky=W, row=18, column=idx)

        ###### Expressions section  #######
        Label(self.mainView, text="Expressions", font='Helvetica 11 bold').grid(row=19)

        for idx, val in enumerate(self.ui_data_structure["Expressions"]):
            Radiobutton(self.mainView, text=val, variable=self.expressions_var, value=val).grid(sticky=W, row=20, column=idx)

        Button(self.mainView, text="Play", command=self._onPlay).grid(row=21, column = 4)
        Button(self.mainView, text="RePlay", command=self._onRePlay).grid(row=21, column=5)


    def _browse_button(self):
        filename = tkFileDialog.askopenfilename(title="Select video:",
                                                filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))

        self.video_path = filename
        self.video_path_var.set(filename)
        print(filename)


    def _onPlay(self):

        selected_subject = self.subject_var.get()
        print selected_subject

        # if not selected_subject:
        #     tkMessageBox.showerror("no subject", "select a subject to continue")
        #     return

        # if selected_subject not in self.results:
        # self.results[selected_subject] = []
        #     playVideo()
        #     return
        #
        # var_6_res = []
        # for item in var_6:
        #     if item.get():
        #         var_6_res.append(item.ui_value)
        #
        # results[selected_subject].append({
        #    'turn': turn.get(),
        #    'start_time' : video_time,
        #    'end_time' : video_time + time_slot,
        #    'Gaze direction': var_1.get(),
        #    'Body orientation':  var_2.get(),
        #    'Body posture':  var_3.get(),
        #    'Head orientation':  var_4.get(),
        #    'Head movement':  var_5.get(),
        #    'Gestures':  var_6_res,
        #    'Emotions':  var_7.get(),
        #    'Expressions':  var_8.get(),
        # })

        self.video_time += time_slot
        if not playVideo():
            self._endOfVideo()

    def _endOfVideo(self):
        endOfVideo()
        ###at the end, print the file
        with open('data.js', 'w+') as outfile:
            json.dump(self.results, outfile)

    def _onRePlay(self):
        return
