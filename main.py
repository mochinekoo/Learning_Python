from typing import List

from ArrayCommand import ArrayCommand
from CommandBase import CommandBase
from FileCommand import FileCommand
from SubClass import SubClass
from SystemCommand import SystemCommand
from ThreadCommand import ThreadCommand
from ThrowCommand import ThrowCommand

subClass = SubClass()


cmd_list: List[CommandBase] = []

subClass.print("てすと")
print("入出力を受け付けてます: \n")

cmd_list.append(SystemCommand())
cmd_list.append(ArrayCommand())
cmd_list.append(ThreadCommand())
cmd_list.append(FileCommand())
cmd_list.append(ThrowCommand())

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