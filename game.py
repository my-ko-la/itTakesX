import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Online asteroids!")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.tracer(0)


pen = turtle.Turtle()
pen.penup()
pen.speed(0)

class Sprite():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x > (SCREEN_WIDTH / 2):
            self.x = -(SCREEN_WIDTH / 2)
        elif self.x < -(SCREEN_WIDTH / 2):
            self.x = (SCREEN_WIDTH / 2)
            
        if self.y > (SCREEN_HEIGHT / 2):
            self.y = -(SCREEN_HEIGHT / 2)
        if self.y < -(SCREEN_HEIGHT / 2):
            self.y = (SCREEN_HEIGHT / 2)

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(self.size, self.size, 0)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()

class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.shape = "triangle"

    def accelerate(self):
        accelX = math.cos(math.radians(self.heading))
        accelY = math.sin(math.radians(self.heading))
        self.dx += accelX
        self.dy += accelY

        pass

    def rot_left(self):
        self.heading += 15

    def rot_right(self):
        self.heading += -15


class Asteroid(Sprite):
    def __init__(self):
        super().__init__()
        self.shape = "circle"


class Missile(Sprite):
    def __init__(self):
        super().__init__()
        self.shape = "circle"
        self.size = 0.2
        self.color = "red"

# Players
p1 = Player()

# Asteroids
as1 = Asteroid()
as1.dx = 1.3
as1.dy = 0.5

# Shot
missile = Missile()

# Game Objects
objects = [p1, as1, missile]

# Keys
wn.listen()
wn.onkeypress(p1.rot_left, "a")
wn.onkeypress(p1.rot_right, "d")
wn.onkeypress(p1.accelerate, "w")

while True:
    wn.update()
    pen.clear()

    for object in objects:
        object.render(pen)
        object.update()


wn.mainloop()