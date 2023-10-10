def nthFIB(n):
    a = 0
    b = 1
    if n <= 1:
        return n
    for _ in range(2, n):
        a, b = b, a + b
        return a


if __name__ == '__main__':
    num = int(input())
    ans = nthFIB(num)
    print(ans)

