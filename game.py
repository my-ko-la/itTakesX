import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Online asteroids!")

wn.setup(1200, 800)


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

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()



# Players
p1 = Player()
p1.render(pen)






wn.mainloop()