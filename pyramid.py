n=10
i=0
for i in range (1,n+1):
    # print(i)
    j=n-i+1
    k=1
    while j>1:
        print("  ",end='')
        j=j-1
    while k<2*i:
        print(' *',end='')
        k=k+1
    print()