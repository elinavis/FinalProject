# # root = Tk(  )
# # for r in range(3):
# #    for c in range(4):
# #       Label(root, text='R%s/C%s'%(r,c),
# #          borderwidth=1 ).grid(row=r,column=c)
# # root.mainloop(  )
#
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
#
# # Tkconstantsroot = Tk()
# # root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# # print (root.filename)
#
# def browse_button():
#     # Allow user to select a directory and store it in global var
#     # called folder_path
#     global folder_path
#     filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
#
#     folder_path.set(filename)
#     print(filename)
#
#
# def switch():
#     global root,frame1
#     frame1.grid_forget()
#     frame2 = Frame(root)
#     frame2.grid(row=0,column=0)
#     turn_var = StringVar()
#     Label(frame2, text="The turn of participant:").grid(row=2, column=1)
#     OptionMenu(frame2, turn_var, 'A', 'B', 'C', 'D').grid(row=2, column=2)
#
#
root = Tk()
newText = Text(root, width=50, height=8, takefocus=0)
newText.grid(row=0, column=0, padx=10, pady=2)

#write to widget
newText.insert(0.0, "Text to insert")
print newText.get()
#
#
mainloop()
#
# #######################################################
# ##### toggle button
# # Window = Tk()
# # Window.title("TekstEDIT")
# # index = 0
# #
# #
# # def onNightMode(b):
# #     global index
# #     if index:
# #         b.config(font=('courier', 12, 'normal'), background='black', fg='green')
# #
# #     else:
# #         b.config(font=('courier', 12, 'normal'), background='green', fg='black')
# #
# #     index = not index
# #
# # b = Button(Window, text='Night-Mode',  command=lambda: onNightMode(b))
# #
# # b.pack(side=LEFT)
# # Window.mainloop()
# #######################################################
#

# mainloopimport json
#
# with open('data.js', 'w+') as outfile:
#     json.dump({"a": 1, "b":2}, outfile)