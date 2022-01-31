from locale import currency


data = input("입력: ")
tokens = data.split()
amount, currency = tokens
amount = float(amount)

if currency == '달러' :
    print(amount * 1167)
elif currency == '엔' :
    print(amount * 1.096)
elif currency == ' 유로' :
    print(amount * 1268)
else:
    print(amount * 171)
