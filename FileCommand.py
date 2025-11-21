from abc import ABC

from CommandBase import CommandBase


class FileCommand(CommandBase, ABC):

    def __init__(self):
        super().__init__()

    def runcmd(self, name: str):
        if name == "file_write":
            file = open("test.txt", "x", encoding="UTF-8") #text.txtを新規作成でUTF-8で書き込む
            file.write("こんにちは\nあいうえお") #文字として書き込む
            file.writelines(["aa", "ii"]) #文字列として書き込む
            file.close()
            print("書き込みが完了しました")
            return True
        return False