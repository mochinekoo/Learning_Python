import subprocess
import sys
import time
from abc import ABC

import psutil

from CommandBase import CommandBase

class SystemCommand(CommandBase, ABC):

    def __init__(self):
        super().__init__()

    def runcmd(self, name):
        print(__name__)
        if name == "cpumem_info":
            time.sleep(2)
            cpu_percent = psutil.cpu_percent(percpu=True)
            mem = psutil.virtual_memory()
            print("CPU", cpu_percent)
            print("Mem", mem.percent)
            return True
        elif name == "run_sh":
            processs = subprocess.run(["F:\\Program Files\\Git\\bin\\bash.exe", "subprocess.sh"], capture_output=True, text=True)
            print(processs.stdout)
            return True
        elif name == "exit":
            print("終了します")
            sys.exit(0)
        return False
