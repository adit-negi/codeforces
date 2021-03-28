a =set(["A", "O", "Y", "E", "U", "I"])
s = input()
ans = ''
for i in s:
    if i.upper() not in a:
        ans += '.'+i.lower()
print(ans)