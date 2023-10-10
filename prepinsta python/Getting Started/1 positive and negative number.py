def checkSign(n):
    if n == 0:
        print('Zero')
    else:
        print('positive' if n > 0 else 'negative')


if __name__ == '__main__':
    num = int(input())
    checkSign(num)
