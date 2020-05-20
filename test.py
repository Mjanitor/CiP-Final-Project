import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels

PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 100

BALL_SIZE = 70

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Flappy Karel')

    # TODO: 1. we now make a paddle
    player = canvas.create_oval(0, CANVAS_HEIGHT, 50, CANVAS_HEIGHT - 50, fill= 'red')

    # Creates a random gap value to pass through
    gap = random.randint(100, CANVAS_HEIGHT // 2)

    rect_top = create_top(canvas, gap)
    rect_bot = create_bot(canvas, gap)

    dx = -5
    dy = 0
    while True:
        # TODO: 2. get the mouse location and react to it
        mouse_x = canvas.winfo_pointerx()
        mouse_y = canvas.winfo_pointery()
        canvas.moveto(player, mouse_x, mouse_y)

        canvas.move(rect_top, dx, dy)
        canvas.move(rect_bot, dx, dy)

        print(canvas.coords(rect_top))

        # Create a new rectangle if off-screen
        if check_offscreen(canvas, rect_top):
            del rect_top
            rect_top = create_top(canvas, gap)

        if check_offscreen(canvas, rect_bot):
            del rect_bot
            rect_bot = create_bot(canvas, gap)

        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50.)


        # TODO: 3. Kill the ball if it hits the rectangles
        if hit_wall(canvas, player, rect_top):
            break

        print(hit_wall(canvas, player, rect_top))

def hit_wall(canvas, player, rect_top):
    # TODO: paddle_coords is of type list. Come to lecture Monday!
    player_coords = canvas.coords(player)
    x1 = player_coords[0]
    y1 = player_coords[1]
    x2 = player_coords[2]
    y2 = player_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1

def create_top(canvas, gap):

    rect = canvas.create_rectangle(CANVAS_WIDTH, 0, CANVAS_WIDTH - 50, gap, fill='blue')

    return rect

def create_bot(canvas, gap):

    rect = canvas.create_rectangle(CANVAS_WIDTH, gap + 150, CANVAS_WIDTH - 50, CANVAS_HEIGHT, fill='blue')

    return rect

def check_offscreen(canvas, rect):
    rect_coords = canvas.coords(rect)
    x2 = rect_coords[2]

    return x2 < 0

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()