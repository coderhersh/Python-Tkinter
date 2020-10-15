from tkinter import *

root = Tk()
cnv = Canvas(root, bg='yellow', height=250, width=300)
line = cnv.create_line(100, 120, 320, 40, fill='green')
arc = cnv.create_arc(180, 150, 80, 210, fill='red')
oval = cnv.create_oval(80, 30, 140, 150, fill='blue')
cnv.pack()
root.mainloop()