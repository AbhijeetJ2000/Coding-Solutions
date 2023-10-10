def sumInRange(a, b):
    ans = int(b * ( b + 1 ) / 2 - a * ( a + 1 ) / 2 + a)
    print(ans)


if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    sumInRange(n1, n2)

