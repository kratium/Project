a = list()
while True:
    number = int(input())
    a.append(number)
    a = [number * 2 for number in a]
    print(a)