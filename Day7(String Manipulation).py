b=True
S=input("Enter string: ")
for i in s:
    if i!='0' or i!='1':
        b=False
if(b):
    print("The given string: "+s+" is a binary code")
else:
    print("The given string: "+s+" is not a binary code")
    