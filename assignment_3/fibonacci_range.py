rng = 100
 
fb = [1,1]

while 1:

    add = (fb[-1]+fb[-2])
    if add <= rng:
        fb.append(add)
    else:
        break

for i in fb:
    print(i)