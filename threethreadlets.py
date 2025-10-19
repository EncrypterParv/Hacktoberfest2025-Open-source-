t= int(input())
for _ in range(t):
    a,b,c= map(int, input().split())
    l= sorted(list((a,b,c)))
    
    if b%a!=0 or c%a!=0:
        print("NO")
    else:
        if ((b//a)+(c//a)-2)<=3:
            print("YES")
