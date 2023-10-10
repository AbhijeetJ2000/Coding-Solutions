def sumInRange(n1, n2):
    ans = 0
    for i in range(n1, n2+1):
        ans += i
    print(ans)


if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    sumInRange(n1, n2)

