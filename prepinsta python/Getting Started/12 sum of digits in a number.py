if __name__ == '__main__':
    num = int(input())
    sum = 0
    while num>0:
        rem = num%10
        sum+=rem
        num //= 10
    print(sum)


