# def isOneDigit(num):
#   return ((num <= 0) and (num < 10))

# def isPallindromeHelper(num, dupNum):
#   if isOneDigit(num): 
#     return num == dupNum % 10

#   if isPallindromeHelper(int(num / 10), dupNum) == False:
#     return -1

#   dupNum = int(dupNum / 10)
#   return num % 10 == dupNum % 10

# def isPallindrome(num):
#   if num < 0:
#     num = -num
  
#   dupNum = num
#   return isPallindromeHelper(num, dupNum)


# print(isPallindrome(1221))

n = int(input("Enter number:"))
temp = n
reversedNum = 0
while n > 0:
    dig = n % 10
    print('dig: ' + str(dig))
    reversedNum = reversedNum * 10 + dig
    print('reversedNum: ' + str(reversedNum))
    n = n // 10
    print('n: ' + str(n))
    print('')
if temp == reversedNum:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")