x = 1
ans = 0
while x <= 50:
    ans += x * x
    x += 1
    ans -= x * x
    x += 1
    
print (ans)

