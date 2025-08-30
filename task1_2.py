print("Enter Input:")
input=input( )

check=['L','U','M','O','S']
ans=list()
k=0
step=0

for i in input:
    step+=1
    if i.upper() in check:
        ans.add(i.upper())
        k=len(ans)
    if k==len(check):
        
        print("earliest step:",step)
        break

else:
    print(-1)

    

        
