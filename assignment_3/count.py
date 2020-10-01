add = 0
count = 0

while 1:

    ent = input('Enter:')

    if ent == 'done':
        break

    try:
        num = int(ent)
        add +=num
        count += 1
    except:
        print('Wrong Input.')
        pass

if count>0:
    print('Sum:',add,'\ncount:',count,'\naverage:',(int(add/count))) 
else:
    print('No inputs.')