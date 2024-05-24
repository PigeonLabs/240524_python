from itertools import combinations

count = 0
num = list(map(int,input()[1:-1].split(",")))
for i in combinations(num,3):
    i = sum(i)
    c = True
    for k in range(2,int(i**0.5)+1):
        if i%k == 0:
            c = False
            break
    if c == True:
         count += 1
print(count)