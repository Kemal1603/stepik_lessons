s, t = [input() for _ in range(2)]
counter = 0

while s not in '':
    if s.startswith(t):
        counter += 1
        s = s[1:]
    else:
        s = s[1:]


print(counter)
