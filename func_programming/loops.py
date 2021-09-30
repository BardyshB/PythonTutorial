# for loop

bar = [1, 2, 3]
for i in bar:
    print(i)


bar = [(1, 2), (2, 3), (3, 4)]
for i, i1 in bar:
    print(i, i1)

# while loop

bar = [1, 2, 3]
while bar:
    print(bar.pop())

bar = [1, 2, 3]

while True:
    if not bar:
        break
    print(bar.pop())
