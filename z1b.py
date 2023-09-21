
n=input("enter a number: ")
str_n=str(n)
if (str_n==str_n[::-1]):
    print("palindrome")
else:
    print("not a palindrome")
for i in range(10):
    if(str_n.count(str(i))>0):
        print(str(i),"appears", str_n.count(str(i))," times")