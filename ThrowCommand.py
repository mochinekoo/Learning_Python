from abc import ABC

from CommandBase import CommandBase


class ThrowCommand(CommandBase, ABC):

    def __init__(self):
        super().__init__()

    def runcmd(self, name):
        print(__name__)
        if name == "throw_cmd":
            try:
                x = 10 / 0
                return True
            except ZeroDivisionError:
                print("ゼロでは割れないよ")
                return True
        elif name == "throw_custom":
            self.print()
            return True
        return False

    def print(self):
        raise CustomError("カスタムなえらーがおきたうお")

class CustomError(Exception):
    def __init__(self, arg=""):
        self.arg = arg