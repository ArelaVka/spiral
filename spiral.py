n = int(input())
m = [[0] * n for i in range(n)]
e=0
i=0
j=0

for j in range(n):
    e+=1
    m[i][j]=e
    
#print("i =", i)
#print("j =", j)
#print("e=", e)
k=n-1
#print("k =", k)

while k >= 1 and e!=n*n:
    while i < k:
        e+=1
        i=i+1
        m[i][j]=e
        print("down")
        print("i =", i)
        print("j =", j)
        print("e=", e)
    while j > (n-1-k):
        e+=1
        j=j-1
        m[i][j]=e
        print("left")
        print("i =", i)
        print("j =", j)
        print("e=", e)
    while i > (n - k):
        e+=1
        i=i-1
        m[i][j]=e
        print("up")
        print("i =", i)
        print("j =", j)
        print("e=", e)
    while j <= (k - 2):
        e+=1
        j=j+1
        m[i][j]=e
        print("right")
        print("i =", i)
        print("j =", j)
        print("e=", e)
    k=k-1

#вывод
for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()
