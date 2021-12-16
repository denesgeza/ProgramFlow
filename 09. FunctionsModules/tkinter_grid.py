import tkinter

from pyparsing import col

# ? .pack => geometry manager
# ? .grid => geometry manager

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title('Hello World')
# ! it works also without the + values
mainWindow.geometry('800x600+8+400')

label = tkinter.Label(mainWindow, text='Hello World')
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=0)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=1)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')
button3 = tkinter.Button(mainWindow, text='button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()

# tkinter._test()