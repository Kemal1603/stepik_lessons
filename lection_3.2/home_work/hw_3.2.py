counter = 0
s, a, b = (input() for _ in range(3))


for i in range(1001):
    if a in s:
        s = s.replace(a, b)
        counter += 1


if counter > 1000:
    print('Impossible')
else:
    print(counter)
