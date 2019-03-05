# *******************************************************************************************************************
# Tkinter Module Notes:
#
# provides access to the tkinter widget tool kit; allows GUI programs to be created; part of the standard Python
# library. Everything in tkinter is a window and objects must be placed in a hierarchy; mainwindow is the root
# window, so everything must be placed within it or within one of the child window.
# Not every window can have children but every window except the root one MUST have a master window;
#
# Pack Geometry Manager:
# - Pack is only useful for very simple layouts and most basic of the three geometry managers.
#
# Place Geometry Manager:
#
# - Weight option is quite important when determining behavior of widgets within cells, unless a weight option has
# been set for a column or row, functions like 'sticky' wont work
# *******************************************************************************************************************

# Pack Examples:

# try:
#     import tkinter
# except ImportError: # this is if you're running Python 2
#     import Tkinter as tkinter
#
# # print(tkinter.TkVersion)
# # print(tkinter.TclVersion)
#
# # tkinter._test()
#
# mainWindow = tkinter.Tk()  # another way to open a window
#
# mainWindow.title("Hello World")
# mainWindow.geometry('640x480+8+400') # values here are width, height, '+' represents distance in pixels from
#                                      # left edge, 2nd '+' is how far from top border down
#
# label = tkinter.Label(mainWindow, text="Hello World")
# label.pack(side='top')
#
# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
#
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n') # fill=tkinter.X, expand=True)  # 'expand=True'code for getting widget to stretch across screen
#                                                        # 'fill=tkinter.X' doesnt do it, although .Y stretches vertically
#
# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)
# button1 = tkinter.Button(rightFrame, text="button1")
# button2 = tkinter.Button(rightFrame, text="button2")
# button3 = tkinter.Button(rightFrame, text="button3")
# # button1.pack(side='top', anchor='n') # when widgets share the same side, they are placed adjacent to one another in the order they
# #                           # were coded
# # button2.pack(side='top', anchor='s')
# # button3.pack(side='top', anchor='e')
#
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')
#
# mainWindow.mainloop() # passes control over to tkinter by calling the mainloop method; mainloop handles all
#                       # the event processing a GUI needs to function.

# *********************************************************************************************************************

# Place Examples:

try:
    import tkinter
except ImportError: # this is if you're running Python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()  # another way to open a window

mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200') # values here are width, height, '+' represents distance in pixels from
# left edge, 2nd '+' is how far from top border down

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0) # fill=tkinter.X, expand=True)  # 'expand=True'code for getting widget to stretch across screen
# 'fill=tkinter.X' doesnt do it, although .Y stretches vertically

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n') # 'sticky' can be used to change the position of the widgets w/in
                                             # their cells
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side='top', anchor='n') # when widgets share the same side, they are placed adjacent to one another
#                                      # in the order they were coded
# button2.pack(side='top', anchor='s')
# button3.pack(side='top', anchor='e')

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop() # passes control over to tkinter by calling the mainloop method; mainloop handles all
# the event processing a GUI needs to function.
