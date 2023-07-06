from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60

def generate_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

background = generate_color()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping-Pong")
clock = time.Clock()


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False