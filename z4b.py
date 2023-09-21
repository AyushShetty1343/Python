#4b
def rom2dec(romanStr):
    romandict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romanrev=list(romanStr)[::-1]
    value=0
    rightval=romandict[romanrev[0]]
    for num in romanrev:
        leftval=romandict[num]
        if leftval<rightval:
            value-=leftval
        else:
            value+=leftval
        rightval=leftval
    return value
romanStr=input("enter a roman number: ")
print(rom2dec(romanStr))