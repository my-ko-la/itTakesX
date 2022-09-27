import turtle
import math
import random

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
        self.lives = 3
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.active = True

    def update(self):
        if self.active:
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
        if self.active:
            pen.goto(self.x, self.y)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.setheading(self.heading)
            pen.stamp()


    def is_collision(self, other):
        x = self.x-other.x
        y = self.y-other.y
        distance = (x**2 + y**2) ** 0.5
        if distance < ((10*self.size)+(10*self.size)):
            return True
        else: 
            return False

    def goto(self, x, y):
        self.x = x
        self.y = y
    
class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.shape = "triangle"
        self.lives = 3
        self.score = 0

    def accelerate(self):
        accelX = math.cos(math.radians(self.heading))
        accelY = math.sin(math.radians(self.heading))
        self.dx += accelX
        self.dy += accelY

    def decelerate(self):
        accelX = math.cos(math.radians(self.heading))
        accelY = math.sin(math.radians(self.heading))
        self.dx -= accelX * 0.3
        self.dy -= accelY * 0.3

    def rot_left(self):
        self.heading += 30

    def rot_right(self):
        self.heading -= 30


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
        self.active = False

    def update(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy
        
            if self.x > (SCREEN_WIDTH / 2):
                self.active = False
            elif self.x < -(SCREEN_WIDTH / 2):
                self.active = False
                
            if self.y > (SCREEN_HEIGHT / 2):
                self.active = False
            if self.y < -(SCREEN_HEIGHT / 2):
                self.active = False

    def fire(self):
        if not self.active:
            self.active = True
            self.x = p1.x
            self.y = p1.y
            self.heading = p1.heading
            self.dx = math.cos(math.radians(self.heading)) * 9
            self.dy = math.sin(math.radians(self.heading)) * 9



# Game Objects
objects = []

# Player(s)
p1 = Player()
objects.append(p1)
# Asteroids

for _ in range(8):
    asteroid = Asteroid()  
    x = random.randint(-500, 500)
    y = random.randint(-375, 375)
    asteroid.goto(x,y)

    dx = random.randint(-2,5) / 20.0    
    dy = random.randint(-2,5) / 20.0    

    asteroid.dx, asteroid.dy = dx, dy
    asteroid.size = random.randint(10,40) / 10.0
    objects.append(asteroid)

# Shot
missile = Missile()
objects.append(missile)

# Controls
wn.listen()
wn.onkeypress(p1.rot_left, "a")
wn.onkeypress(p1.rot_right, "d")
wn.onkeypress(p1.accelerate, "w")
wn.onkeypress(p1.decelerate, "s")
wn.onkeypress(missile.fire, "space")

while True:
    wn.update()
    pen.clear()

    for i in range(p1.lives):
        pen.goto(-( SCREEN_WIDTH / 2 )+ 20 + 30 * i, (SCREEN_HEIGHT / 2)-50)
        pen.shape("triangle")
        pen.shapesize(0.7,0.7,0)
        pen.setheading(90)
        pen.stamp()

    for object in objects:
        object.render(pen)
        object.update()

    for object in objects:
        if isinstance(object, Asteroid):
            if p1.is_collision(object):
                p1.lives -= 1 
                p1.goto(0,0)
                object.goto(100,100)

                if p1.lives <= 0:
                    p1.active = False
                

            if missile.active and missile.is_collision(object):
                print("Aster ded")
                missile.active = False
                p1.score += 10
                object.goto(200,200)

wn.mainloop()