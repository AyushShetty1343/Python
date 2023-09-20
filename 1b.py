num = input("Enter the Number")
rev = num
if (rev == rev[::-1]):
    print("The Number is Palindrome", num)
else:
    print("The Number  is not Palindrome", num)
for i in set(num):
    print(i, "appears", num.count(str(i)), "times")
