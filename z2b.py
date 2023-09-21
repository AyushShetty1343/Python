#2b
def bin2dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec

def oct2hex(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*8**i
        i+=1
    hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    oct2hex=' '
    while dec>0:
        rem=dec%16
        oct2hex=hexa[rem]+oct2hex
        dec=dec//16
    return oct2hex

num1=input("enter a binary num: ")
print(bin2dec(num1))
num2=input("enter a octal num: ")
print(oct2hex(num2))