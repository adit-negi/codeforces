n, k = input().split()
n, k =int(n), int(k)
l = list(map(int,input().split()))
k_score = l[k-1]
res = 0
for i in l:
    if i>0 and i>=k_score:
        res+=1
print(res)