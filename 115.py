data = input("입력값: ")
data = int(data)
data = data - 20
if data < 0:
    print(0)
elif data > 255:
    print(255)
else:
    print(data)