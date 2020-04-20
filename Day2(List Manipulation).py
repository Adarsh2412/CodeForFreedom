def test():
    n=int(input())
    if n<1 or n>200000:
        return
    A=list(range(0,n))
    B=list(range(0,n))
    s1=input()
    s2=input()
    A=s1.split(' ')
    B=s2.split(' ')
    for i in range(0,n):
        for j in range(0,n):
            if A[i]==A[j] or i==j:
                if int(B[i])<int(B[j]):
                    B[i]=B[j]
    for i in B:
        print(i,end=" ")
test()
