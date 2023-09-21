#8a
class PaliStr:
    def __init__(self):
        self.ispali=False
    def chkpalindrome(self,mystr):
        if mystr==mystr[::-1]:
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
    
class PaliInt:
    def __init__(self):
        self.ispali=False
    def chkpalindrome(self,val):
        temp=int(val)
        rev=0
        while temp!=0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        if (int(val)==rev):
            self.ispali=True
        else:
            self.ispali=False
        return self.ispali
mystr=input("enter a string: ")
mystrobj=PaliStr()
if mystrobj.chkpalindrome(mystr):
    print("palindrome")
else:
    print("not a palindrome")
    
val=input("enter an integer: ")       
valobj=PaliInt()
if valobj.chkpalindrome(val):
    print("palindrome")
else:
    print("not a palindrome")