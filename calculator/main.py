a = float(input("first num > "))
b = float(input("second num > "))
command_list = ['+','-','/','*','**']

print('Commands' + str(command_list))

c = input("what will we do > ")
res = None

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
else:
    print('Not know command')

print("Task > " + str(int(a)) + " " + str(c) + " " + str(int(b)))
print("This is result = " + str(int(res)))




