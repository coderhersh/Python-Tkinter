from tkinter import *

def show():
    print('True')

root = Tk()
root.title('Button')
root.geometry('300x300')
root.minsize(100, 100)

btn = Button(root, text='Button', command = show)
btn.pack(side='bottom')

root.mainloop()
