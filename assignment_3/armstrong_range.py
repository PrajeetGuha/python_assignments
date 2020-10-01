
rng = 1000
for i in range(1,rng+1):

    num = str(i)
    sum = 0

    for j in num:

        sum = sum + int(j)**3

    if sum == i:
        print(i)