a = int(input('Enter a: '))
b = int(input('Enter b: '))
s1 = 0
s2 = 0
s3 = 0
total = 0
for i in range(a, b):
    s1 += i
    total += 1
    s2 = s1 / total
    pass
for g in range(a, b):
    a += 1
    if s2 % a == 0:
        s3 += a
        continue
print(s3)
