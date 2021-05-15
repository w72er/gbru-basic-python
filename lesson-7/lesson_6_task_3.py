# Работа над ошибкой:
# > если инициализатор повторяет родительский, то его незачем прописывать
# > в дочернем классе

# реально наследуются все магические методы, в том числе и инициализатор :)

class Worker:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Position(Worker):
    def __init__(self, name):  # наследуется?
        super().__init__(name)


class Position2(Worker):
    pass


p = Position('Ivanov')
print(p)
p2 = Position2('Ivanov2')
print(p2)
