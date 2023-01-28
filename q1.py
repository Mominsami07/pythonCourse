a= int(input('a : '))
b= int(input('b : '))
k= int(input('k : '))

for n in range (a,b):
    sum=0
    for i in range(a,n+1):
        sum+=i
    if sum<k:
        print (n, end=' ')
        
## TR: 10 pts.