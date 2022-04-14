for i in range (1, 101):
    if i % 7 == 0 or '7' in str(i):
        continue
    print(i)

for i in range (1, 101):
    if not(i % 7 == 0 or '7' in str(i)):
        print(i)


