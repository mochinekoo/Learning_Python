import threading
import time
from abc import ABC

from CommandBase import CommandBase


class ThreadCommand(CommandBase, ABC):

    def __init__(self):
        super().__init__()
        self.flag = True
        self.count = 0
        self.thread = None

    def runcmd(self, name: str):
        if name == "thread_cmd":
            self.thread = threading.Thread(target=self.timer)
            self.thread.start()
            return True
        elif name == "thread_stop":
            self.flag = False
            self.thread.join()
            pass
        return False

    def timer(self):
        while self.flag:
            print(self.count)
            time.sleep(1)
            self.count+=1
