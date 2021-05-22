from beartype import beartype
from typing import Type


class Parent:
    def __init__(self):
        self.par = -1

    def parent_method(self):
        print("parent_method")


@beartype
def check_parent_arg(p: Parent):
    p.parent_method()


check_parent_arg(Parent())


# beartype.roar.BeartypeCallHintPepParamException: @beartyped check_parent_arg()
# parameter p="1" violates type hint <class '__main__.Parent'>, as value "1"
# not <class "__main__.Parent">.
# check_parent_arg(1)

class Daughter(Parent):
    def __init__(self):
        super().__init__()
        self.dau = 'dau'

    pass


def check_daughter_arg(d: Daughter):
    print(d.dau)


class Car:
    pass


check_parent_arg(Daughter())
check_daughter_arg(Daughter())
check_daughter_arg(Parent())
