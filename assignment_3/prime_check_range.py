rng = 1000
for i in range(2,rng+1):

    prime = True

    for j in range(2,i):

        if i%j == 0:
            prime=False
            break

    if prime:
        print(i)