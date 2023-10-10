if __name__ == '__main__':
    num = input()
    isPalindrome = True
    for i in range(0, len(num)):
        if num[i] != num[len(num)-1-i]:
            isPalindrome = False
            break
    if isPalindrome:
        print('Palindrome')
    else:
        print('Not a palindrome')



