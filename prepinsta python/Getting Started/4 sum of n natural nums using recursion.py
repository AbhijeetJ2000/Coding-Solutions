def n_Natural_nums_sum(n):
    if n==0:
        return 0
    sum = n + n_Natural_nums_sum(n-1)
    return sum


if __name__ == '__main__':
    num = input()
    ans = n_Natural_nums_sum(int(num))
    print(ans)

