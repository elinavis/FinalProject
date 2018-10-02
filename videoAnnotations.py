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
        self.name_var = StringVar()

        self.subject_var = StringVar()
        self.turn_var = StringVar()

        self.gaze_direction_var = StringVar()
        self.gaze_options_var = StringVar()
        self.body_orientation_var = StringVar()
        self.body_posture_var = StringVar()
        self.head_orientation_var = StringVar()
        self.head_movement_var = StringVar()
        self.gesture_var = StringVar()
        self.emotions_var = StringVar()
        self.expressions_var = StringVar()

        self.point_at_var = IntVar()
        self.point_at_options_var = StringVar()

        self.look_for_approval_of_var = IntVar()
        self.look_for_approval_of_options_var = StringVar()

        self.show_something_to_someone_var = IntVar()
        self.show_something_to_someone_options_var = StringVar()

        self.no_action_at_turn_var = IntVar()
        self.text = Text(self.mainView, width=25, height=6, takefocus=0, bg= "gray")

        self.ui_data_structure = {}
        self.ui_data_structure["Gaze direction"] = ["A", "B", "C", "D" ,"Up", "Down", "Aside", "Neutral", "Center of Table"]
        self.ui_data_structure["Body orientation"] = ["A", "B", "C", "D","Neutral"]
        self.ui_data_structure["Body posture"] = ["Leaning Front", "Leaning Back", "Jumpy", "Stiff", "Neutral"]
        self.ui_data_structure["Head orientation"] = ["A", "B", "C", "D" ,"Neutral"]
        self.ui_data_structure["Head movement"] = ["Nodding", "Shaking", "Tilting","Neutral"]
        self.ui_data_structure["Gestures"] = ["Hand palms together", "Arms folded", "head leaning on hand", "hands touching face/body", "Play with hands", "Clap hands", "Thumbs down", "Thumbs up", "Disagreeing hand", "none of the above"]
        self.ui_data_structure["Emotions"] = ["Serious", "Bored", "Attentive" , "Skeptical", "none of the above"]
        self.ui_data_structure["Expressions"] = ["Smile","Sour face","Laugh","Yawn", "Aversion", "Eyebrows raised/lowered", "Grimase", "none of the above"]

        self._createFirstView()
        self._createMainView()


    def _createFirstView(self):

        Label(self.firstView, text="Select the video to annotate:").grid(row =0, column = 0)
        Button(self.firstView, text="Browse", command=self._browse_button).grid(row=1, column=3)
        Label(self.firstView, textvariable= self.video_path_var).grid(row=1, column=0)

        Label(self.firstView, text= "exp. number:").grid(row=2, column=0)
        OptionMenu(self.firstView, self.exp_number_var, *range(1,12) ).grid(row=2, column=2)

        Label(self.firstView, text="Round number").grid(row=3, column=0)
        OptionMenu(self.firstView, self.round_var, 0, 1).grid(row=3, column=2)

        Label(self.firstView, text="Name").grid(row=4, column=0)
        OptionMenu(self.firstView, self.name_var, "Julia", "Elina").grid(row=4, column=2 , sticky="ew")

        Button(self.firstView, text="Submit", command=self._goToMainView).grid(row=4, column=3)


    def _createMainView(self):

        Label(self.mainView, text="Participant that is being watched:").grid(row=1, column=0, sticky="e")
        OptionMenu(self.mainView, self.subject_var, 'A', 'C', 'D').grid(row=1, column=1)
        Button(self.mainView, text="Go", command=self._onGo).grid(row=1, column=2)

        self.mainView.grid_rowconfigure(2, minsize=25)

        Label(self.mainView, text="The turn of participant:").grid(row=3, column=0, sticky="e")
        OptionMenu(self.mainView, self.turn_var, 'A', 'B', 'C', 'D').grid(row=3, column=1)

        ###### Gaze direction section  #######
        Label(self.mainView, text="Gaze direction:" ).grid(row=5, column = 0, sticky="e")
        OptionMenu(self.mainView, self.gaze_direction_var, *self.ui_data_structure["Gaze direction"]).grid(row=5, column=1, sticky="ew")

        Label(self.mainView, text="Behavior:" ).grid(row=5, column = 3, sticky="e")
        OptionMenu(self.mainView, self.gaze_options_var, 'Gaze', 'Stare').grid(row=5, column=4, sticky="ew")

        ###### Body orientation section  #######
        Label(self.mainView, text="Body orientation:").grid(row=7, column = 0, sticky="e")
        OptionMenu(self.mainView, self.body_orientation_var, *self.ui_data_structure["Body orientation"]).grid(row=7, column=1, sticky="ew")

        ###### Body posture section  #######
        Label(self.mainView, text="Body posture:" ).grid(row=9, column=0, sticky="e")
        OptionMenu(self.mainView, self.body_posture_var, *self.ui_data_structure["Body posture"]).grid(row=9, column=1, sticky="ew")

        ###### Head orientation section  #######
        Label(self.mainView, text="Head orientation:").grid(row=11, column=0, sticky="e")
        OptionMenu(self.mainView, self.head_orientation_var, *self.ui_data_structure["Head orientation"]).grid(row=11, column=1, sticky="ew")

        ###### Head movement section  #######
        Label(self.mainView, text="Head movement:").grid(row=13, column=0, sticky="e")
        OptionMenu(self.mainView, self.head_movement_var, *self.ui_data_structure["Head movement"]).grid(row=13, column=1, sticky="ew")

        ###### Gestures section  #######
        Label(self.mainView, text="Gestures:").grid(row=15, column=0, sticky="e")
        OptionMenu(self.mainView, self.gesture_var, *self.ui_data_structure["Gestures"]).grid(row=15, column=1, sticky="ew")

        ###### Emotions section  #######
        Label(self.mainView, text="Emotions").grid(row=17, column=0, sticky="e")
        OptionMenu(self.mainView, self.emotions_var, *self.ui_data_structure["Emotions"]).grid(row=17, column=1, sticky="ew")

        ###### Expressions section  #######
        Label(self.mainView, text="Expressions:").grid(row=19, column=0, sticky="e")
        OptionMenu(self.mainView, self.expressions_var, *self.ui_data_structure["Expressions"]).grid(row=19, column=1, sticky="ew")

        ###### Action at turn  #######
        self.mainView.grid_rowconfigure(20, minsize=25)

        Label(self.mainView, text="Action at turn", font='Helvetica 13').grid(row=21)

        #####
        Checkbutton(self.mainView, text="Point at: ", variable=self.point_at_var).grid(sticky=W, row=22 , column = 0)
        OptionMenu(self.mainView, self.point_at_options_var, 'A', 'B', 'C', 'D').grid(row=22, column=1)

        Checkbutton(self.mainView, text="Look for approval of: ", variable=self.look_for_approval_of_var).grid(sticky=W, row=23, column=0)
        OptionMenu(self.mainView, self.look_for_approval_of_options_var, 'A', 'B', 'C', 'D').grid(row=23, column=1)

        Checkbutton(self.mainView, text="Show something to participant: ", variable=self.show_something_to_someone_var).grid(sticky=W, row=24, column=0)
        OptionMenu(self.mainView, self.show_something_to_someone_options_var, 'A', 'B', 'C', 'D').grid(row=24, column=1)

        Checkbutton(self.mainView, text="No action at turn ", variable=self.no_action_at_turn_var).grid(sticky=W, row=25, column=0)

        ###### Free text  #######
        Label(self.mainView, text="Free text:").grid(row=26, column =0)

        self.text.grid(row=26, column=1)

        Button(self.mainView, text="Play", command=self._onPlay).grid(row=30, column = 0)
        # Button(self.mainView, text="RePlay Current Video", command=self._onRePlay).grid(row=30, column=4)
        Button(self.mainView, text="Play New Video", command=self._onPlayNewVideo).grid(row=30, column=4)


    def _browse_button(self):
        filename = tkFileDialog.askopenfilename(title="Select video:",
                                                filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))

        self.video_path = filename
        self.video_path_var.set(filename)
        print(filename)


    def _onPlay(self):

        selected_subject = self.subject_var.get()

        if not selected_subject:
            tkMessageBox.showerror("no subject", "select a subject to continue")
            return

        if selected_subject not in self.results:
            self.results[selected_subject] = {}

        annotation = {
            'turn of': self.turn_var.get(),
            'start_time' : self.video_time,
            'end_time' : self.video_time + time_slot,
            'Gaze direction': self.gaze_direction_var.get(),
            'Gaze behavior': self.gaze_options_var.get(),
            'Body orientation':  self.body_orientation_var .get(),
            'Body posture':  self.body_posture_var .get(),
            'Head orientation':  self.head_orientation_var.get(),
            'Head movement':  self.head_movement_var .get(),
            'Gestures':  self.gesture_var.get(),
            'Emotions':  self.emotions_var .get(),
            'Expressions':  self.expressions_var.get(),
        }

        if self.point_at_var.get():
            annotation["Point at"] = self.point_at_options_var.get()

        if self.look_for_approval_of_var.get():
            annotation["Look for approval of"] = self.look_for_approval_of_options_var.get()

        if self.show_something_to_someone_var.get():
            annotation["Show something to participant"] = self.show_something_to_someone_options_var.get()

        if self.no_action_at_turn_var.get():
            annotation["No action at current turn"] = True

        if self.text.get(1.0, END) != "\n":
            annotation["Additional input"] = self.text.get(1.0, END)
            self.text.delete('1.0', END)

        self.results[selected_subject][self.video_time] = annotation

        self.video_time += time_slot

        if not playVideo():
            tkMessageBox.showinfo("End of Video", "The video ended.")
            self._endOfVideo()

    def _endOfVideo(self):
        endOfVideo()

        # at the end, print the file
        fileName = "./" + self.name_var.get() + "_" + self.exp_number_var.get() + "_" + self.round_var.get() + "_".join(self.results.keys()) + ".json"
        with open(fileName, 'w+') as outfile:
            json.dump(self.results, outfile)

    def _onGo(self):
        self.turn_var.set("A")
        self.video_time = 0
        startVideo(self.video_path_var.get())
        playVideo()


    def _onPlayNewVideo(self):
        destroy()
        self.results = {}
        self.video_path_var.set("")
        self.mainView.grid_forget()
        self.firstView.grid(row=0, column=0)

    def _goToMainView(self):
        self.firstView.grid_forget()
        self.mainView.grid(row=0, column = 0)
        startVideo(self.video_path_var.get())
        showVideo()

        self.video_time = 0
        self.turn_var.set("A")
        self.gaze_options_var.set("Gaze")

    def start(self):
        self.firstView.grid(row=0, column = 0)
        self.root.mainloop()
