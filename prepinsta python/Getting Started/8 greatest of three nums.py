def greatOfThreeNums(n1, n2, n3):
    ans = n1 if n1 > n2 else n2
    ans = n3 if n3 > ans else ans
    print(ans)


if __name__ == '__main__':
    n1, n2, n3 = int(input()), int(input()), int(input())
    greatOfThreeNums(n1, n2, n3)


