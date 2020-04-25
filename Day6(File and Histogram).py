fname=input("Enter Nae of file: ")
fh = open(fname)
count = dict()
for line in fh:
    line=line.rstrip()
    if line.startswith("From "):
        line=line[5:]
        line=line.split(" ")
        count[line[0]]=count.get(line[0],0)+1
bigword=None
bignumber=None
for key,value in count:
    if bignumber==None or bignumber>value:
        bigword=key
        bignumber=value
print(bigword+" "+bignumber)
