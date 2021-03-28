m,n = input().split()
m,n = int(m), int(n)
if m%2==0:
    print((m//2)*n)
else:
    ans = (m//2)*n
    ans += n//2
    print(ans)