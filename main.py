from typing import List

from ArrayCommand import ArrayCommand
from CommandBase import CommandBase
from SubClass import SubClass
from SystemCommand import SystemCommand
from ThreadCommand import ThreadCommand

subClass = SubClass()


cmd_list: List[CommandBase] = []

subClass.print("てすと")
print("入出力を受け付けてます: \n")

cmd_list.append(SystemCommand())
cmd_list.append(ArrayCommand())
cmd_list.append(ThreadCommand())

while True:
    i = input()
    end_result = False
    for cmd in cmd_list:
        cmd_result = cmd.runcmd(i)
        if cmd_result:
            end_result = True

    if not end_result:
        print("コマンドが見つかりませんでした")

    print("\n")