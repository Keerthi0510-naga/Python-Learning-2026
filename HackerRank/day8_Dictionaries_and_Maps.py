n = int(input())
phone_book = {}

for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone

try:
    while True:
        name = input()
        if name in phone_book:
            print(name + "=" + phone_book[name])
        else:
            print("Not found")
except EOFError:
    pass