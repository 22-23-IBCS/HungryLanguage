import turtle
import math

class Artist:

    def __init__(self, t):
        self.t = t
    
    def Triangle(self, size = 100):
        for i in range(3):
            self.t.forward(size)
            self.t.left(120)

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def Square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def Circle(self, size = 1):
        self.t.left(90)
        for i in range(360):
            self.t.forward(size)
            self.t.left(1)
            
    def Circle2(self, size = 1):
        self.t.left(90)
        s = math.sqrt(2*size*size*(1-math.cos(1)))
        for i in range(360):
            self.t.forward(s)
            self.t.left(1)

    def Polygon(self, n, size = 50):
        for i in range(n):
            self.t.forward(size)
            self.t.left(360/n)

    def Star(self, size = 100):
        self.t.left(36)
        for i in range(5):
            self.t.forward(size)
            self.t.left(144)

        
def main():
    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle example")

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(3)


    art = Artist(t)
    
    #art.Circle()
    art.move(-100, 100)
    art.Circle2()
    art.move(-100,-100)
    art.Polygon(5)
    art.move(100,100)
    art.Polygon(9)
    art.move(100,-100)
    art.Triangle()
    art.move(-10,-20)
    art.Star()

    #t.forward(150)
    #t.right(90)
if __name__ == "__main__":
    main()
