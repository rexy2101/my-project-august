a=[2,3,6,4,1,3,9,8,7]
print(a)
for i in a:
    if i%2==0:
        print('{} is a prime number'.format(i))
    else:
        print('odd')