a = float(input("first num > "))
b = float(input("second num > "))
c = input("what will we do > ")
res = None

if c == '+':
    res = a + b
elif c == '-':
    res = a - b
elif c == '*':
    res = a * b
elif c == ':' or c == '/':
    res = a / b
else:
    print("Not found command")

print("Task > " + str(int(a)) + " " + str(c) + " " + str(int(b)))
print("This is result = " + str(int(res)))