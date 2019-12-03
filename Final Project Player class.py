import graphics as g

class Player:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
        self.draw()
        
    # Maybe do some sort of nicer graphic for the player eventually??
    def draw(self):
        self.object = g.Circle(g.Point(self.x, self.y), 40)
        self.object.setFill("red")
        self.object.draw(w)
        
    # Need collision detection
    def control(self, key):
        self.key = key
        if key == "Up":
            self.object.move(0, -5)
        if key == "Down":
            self.object.move(0, 5)
        if key == "Left":
            self.object.move(-5, 0)
        if key == "Right":
            self.object.move(5, 0)