#control digit
n = int(input("Enter a number: "))
while n > 9:
    res = 0
    while n > 0:
        res += (n % 10)
        n = n // 10
    n = res

print(n)
