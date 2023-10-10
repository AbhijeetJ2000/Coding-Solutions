def checkPrime(num, i=2):
    if num <= 1:
        return False
    if i > num // 2:
        return True
    if num % i == 0:
        return False
    else:
        return checkPrime(num, i+1)


if __name__ == '__main__':
    num = int(input())
    isPrime = checkPrime(num)
    if isPrime:
        print('Prime number')
    else:
        print('Non-Prime number')



