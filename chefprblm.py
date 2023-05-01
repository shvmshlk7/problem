problem = list(map(int,input().split()))
count = 0
for i in problem:
    if i>=10:
        count = count + 1
print(count)
