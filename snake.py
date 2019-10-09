from tkinter import *
from random import random
from time import sleep

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

snake = [(3, 3), (4, 3), (5, 3), (6, 3)]


def printSquare(x, y, app=False):
    global w

    if(app):
        w.create_rectangle(x*20, y*20, x*20 + 20,
                           y * 20 + 20, fill="red")
    else:
        w.create_rectangle(x*20, y*20, x*20 + 20,
                           y * 20 + 20, fill="black")


def drawCanvas():
    global w
    global snake
    global apple

    w.delete("all")

    appleX, appleY = apple
    printSquare(appleX, appleY, app=True)

    for x, y in snake:
        printSquare(x, y)


direction = 0

apple = (10, 10)


def moveSnake():
    global snake
    global apple

    x, y = snake[-1]
    if(direction == 0):
        snake.append((x + 1, y))

    if(direction == 1):
        snake.append((x - 1, y))

    if(direction == 2):
        snake.append((x, y + 1))

    if(direction == 3):
        snake.append((x, y - 1))

    appleX, appleY = apple

    if(x == appleX and y == appleY):
        apple = (int(random() * 25), int(random() * 25))
    else:
        del snake[0]


locked=False
def setUp(event):
    global direction
    global locked

    if(direction != 2 and not locked):
        direction = 3
        locked = True


def setDown(event):
    global direction
    global locked

    if(direction != 3 and not locked):
        direction = 2
        locked = True


def setRight(event):
    global direction
    global locked

    if(direction != 1 and not locked):
        direction = 0
        locked = True


def setLeft(event):
    global direction
    global locked

    if(direction != 0 and not locked):
        direction = 1
        locked = True


master.bind('<s>', setDown)
master.bind('<w>', setUp)
master.bind('<d>', setRight)
master.bind('<a>', setLeft)


def task():
    global locked
    
    #canvasMap[int(random() * 24)][int(random() * 24)] = 1
    moveSnake()
    drawCanvas()

    locked = False

    master.after(200, task)  # reschedule event in 2 seconds


task()

mainloop()
