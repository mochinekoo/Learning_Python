import sys

from SubClass import SubClass

subClass = SubClass()
number_list = [10, 20, 30, 40]

subClass.print("てすと")
print("入出力を受け付けてます: \n")

while True:
    i = input()
    if i.lower() == 'exit':
        print("終了します")
        sys.exit(0)
    elif i.lower() == 'number_list':
        print("3番目の要素は：" + str(number_list[3]) + "です")
    print("\n")