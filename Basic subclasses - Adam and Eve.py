class Human:
    def __init_(self):
        pass


class Man(Human):
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        self.name = name


def God():
    Adam = Man("Adam")
    Eva = Woman("Eva")
    return [Adam, Eva]
