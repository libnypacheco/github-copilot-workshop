a = [3, 2, 1, 6, 10]
b = []

running_total = 0
for num in a:
    running_total += num
    b.append(running_total)

print(b)