if __name__ == '__main__':
    num = int(input())
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print('non-prime')
    else:
        print('prime')



