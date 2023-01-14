a,b,c=sorted(map(int,input().split()))
print(((1000+100*b,c*100)[a!=b and b!=c],10000+1000*a)[a==c])