import random
class RandomWalk:
    def pick_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b
    def pick_length(self):
        length = random.randint(1, 40)
        return length
    def random_walk(self,turtle,times):
        directions = [0, 90, 180, 270]
        for i in range(times):
            turtle.color(self.pick_color())
            turtle.setheading(random.choice(directions))
            turtle.forward(self.pick_length())
