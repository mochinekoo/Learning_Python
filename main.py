import sys

from SubClass import SubClass

subClass = SubClass()

subClass.print("てすと")
print("入出力を受け付けてます: \n")

while True:
    i = input()
    if i.lower() == 'exit':
        print("終了します")
        sys.exit(0)
    print("\n")