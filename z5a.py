#5a
import re
def isphonenumber(phnum):
    if(len(phnum)!=12):
        return False
    for i in range(len(phnum)):
        if i==3 or i==7:
            if phnum[i]!='-':
                return False
            else:
                if phnum[i].isdigit()==False:
                    return False
        return True
def chkphonenumber(phnum):
    num_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if num_pattern.match(phnum):
        return True
    else:
        return False

phnum=input("enter a phone number: ")
print("without using regular expression")
if isphonenumber(phnum):
    print("valid")
else:
    print("invalid")

print("using regular expression")
if chkphonenumber(phnum):
    print("valid")
else:
    print("invalid")