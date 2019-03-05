import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size  # dividing by 100 prevents 'y' values from running off the screen
        plot(page, x, y)
        plot(page, -x, y)

# Modify the circle function so that it allows the color of the circle to be specified and defaults
# to red if a color is not given. You may want to review the previous lectures about named parameters
# and default values.
# - for this challenge he meant modify the code, so that within the code, color of the circle could
# be specified.  In essence, create another parameter 'color' you see below; and if you define it
# that becomes the default value if not specified in your code.


def circle(page, radius, g, h, color="red"):
# def circle(page, radius, g, h):
    # page.create_oval(g + radius, h + radius, g - radius, h - radius, outline="red", width=2)
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)

# for x in range(g * 100, (g + radius) * 100): # multiplying by 100 allows the program to plot
    #                                              # 100 times as many points increasing accuracy but
    #                                              # it does take longer
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)
# draw_axes(canvas2)

# for x in range(-100, 100):
#     y = parabola(x)
#     plot(canvas, x, -y)  # negative value of 'y' flips the graph so it's rightside up.  Graph plot prints out
                         # upside down because the canvas coordinate system has the y axis starting at the top
                         # with increasing #s moving down the screen, where traditional graph plotting have the 'y'
                         # values moving up from the axes.
                         # Where a variable is visible and can be used is called 'Scope.';
                         # A function can use the variables from the main program but the main program cannot see
                         # variables that are local to the function

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
