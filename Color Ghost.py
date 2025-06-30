import random
class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = colors[random.randrange(0, len(colors))]

ghost = Ghost()
print(ghost.color)
