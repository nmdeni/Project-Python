a = float(input("first num > "))
b = float(input("second num > "))
command_list = ['+','-','/','*','**']

print('Commands' + str(command_list))

c = input("what will we do > ")
res = None

for i in command_list:
    if c == i:
        if c == '+':
            res = a + b
        elif c == '-':
            res = a - b
        elif c == '*':
            res = a * b
        elif c == '/':
            res = a / b
        elif c == '**':
            res = a ** b

        print("Task > " + str(int(a)) + " " + str(c) + " " + str(int(b)))
        print("This is result = " + str(int(res)))
        break
    else:
        continue

