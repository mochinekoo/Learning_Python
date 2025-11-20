import subprocess
import sys
import time
import psutil

from SubClass import SubClass

subClass = SubClass()
number_list = [10, 20, 30, 40]

cpu_percent = psutil.cpu_percent(percpu=True)
mem = psutil.virtual_memory()

subClass.print("てすと")
print("入出力を受け付けてます: \n")

while True:
    i = input()
    if i.lower() == 'exit':
        print("終了します")
        sys.exit(0)
    elif i.lower() == 'number_list':
        print("3番目の要素は：" + str(number_list[3]) + "です")
    elif i.lower() == 'cpumem_info':
        time.sleep(2)
        cpu_percent = psutil.cpu_percent(percpu=True)
        print("CPU", cpu_percent)
        print("Mem", mem.percent)
    elif i.lower() == 'run_sh':
        processs = subprocess.run(["F:\\Program Files\\Git\\bin\\bash.exe", "subprocess.sh"], capture_output=True, text=True)
        print(processs.stdout)
    print("\n")