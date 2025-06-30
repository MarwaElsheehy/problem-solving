class Hero(object):
    def __init__(self, name, position, health, damage, experience):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience

myHero = Hero("Hero", "00", "100", "5", "0")
print(myHero.name)
