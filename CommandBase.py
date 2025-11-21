from abc import abstractmethod, ABC, ABCMeta

#　これはコメントです
class CommandBase(ABC, metaclass=ABCMeta):
    """ コマンド用のクラス
    """

    def __init__(self):
        pass

    @abstractmethod
    def runcmd(self, name):
        """ コマンドを実行する関数
        :param name: 実行したいコマンド名
        :return: 実行に成功した場合はTrue、失敗した場合はFalseを返す
        """

        pass