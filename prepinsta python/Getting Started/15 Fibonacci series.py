if __name__ == '__main__':
    num = int(input())
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2, num):
        sum = a + b
        a = b
        b = sum
        print(sum, end=" ")

