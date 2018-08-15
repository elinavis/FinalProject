# root = Tk(  )
# for r in range(3):
#    for c in range(4):
#       Label(root, text='R%s/C%s'%(r,c),
#          borderwidth=1 ).grid(row=r,column=c)
# root.mainloop(  )

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

# Tkconstantsroot = Tk()
# root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))

    folder_path.set(filename)
    print(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

mainloop()

#######################################################
##### toggle button
# Window = Tk()
# Window.title("TekstEDIT")
# index = 0
#
#
# def onNightMode(b):
#     global index
#     if index:
#         b.config(font=('courier', 12, 'normal'), background='black', fg='green')
#
#     else:
#         b.config(font=('courier', 12, 'normal'), background='green', fg='black')
#
#     index = not index
#
# b = Button(Window, text='Night-Mode',  command=lambda: onNightMode(b))
#
# b.pack(side=LEFT)
# Window.mainloop()
#######################################################

