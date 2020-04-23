import re
fname=input("Enter name of file: ")
sum=0
fh=open(fname)
for line in fh:
    a=re.findall('[0-9]+',line)
    if len(a) ==0:
        continue
    for j in a:
        sum+=int(j)
print(sum)
