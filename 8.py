class A:
    def Pal(self, val: str):
        if (val != val[::-1]):
            print("Not palindrome")
        else:
            print("Is Palindrome")


class B(A):
    def Pal(self, val: int):
        super().Pal(str(val))


strobj = A()
stringg = input("Input String")
A.pal(stringg)
intobj = B()
intt = int(input("Input Number"))
B.pal(intt)
