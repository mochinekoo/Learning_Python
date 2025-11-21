from abc import abstractmethod, ABC, ABCMeta


class CommandBase(ABC, metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def runcmd(self, name):
        pass