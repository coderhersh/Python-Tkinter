from tkinter import *

root = Tk()
root.title('Root')
# width X height
root.geometry('320x320')
# root.minsize(50, 50)
# photo = PhotoImage(file='10-7.png')

# L = Label(image=photo)
# L.pack()

"""
Label Attributes:
text, font, fg, bg, padx, pady, relief(border styling)
font = tuple, string(with space)
relief(border styling) =
"""
tup = ("comicsansms", 10, 'bold')
label = Label(root, text='Meow!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!,!',
              fg='black', bg='yellow',
              font=tup, padx=113, pady=94)
# Pack Options
# .pack(anchor='ne')
# side = top, bottom, left, right
# fill = X(spreads horizontally), Y, BOTH
# padx, pady = padding
label.pack()
root.mainloop()
