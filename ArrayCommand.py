from abc import ABC

from CommandBase import CommandBase


class ArrayCommand(CommandBase, ABC):

    def __init__(self):
        super().__init__()

    def runcmd(self, name: str):
        number_list = [10, 20, 30, 40]
        if name == "number_list":
            print("3番目の要素は：" + str(number_list[3]) + "です")
            print(__name__)
            return True
        return False