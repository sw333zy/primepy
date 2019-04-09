'''A prime number is an integer, or whole number, that has only two factors — 1 and itself. 
Put another way, a prime number can be divided evenly only by 1 and by itself. Prime numbers 
also must be greater than 1. For example, 3 is a prime number, because 3 cannot be divided evenly 
by any number except for 1 and 3. However, 6 is not a prime number, because it can be divided evenly by 2 or 3.'''

for i in range(1,100,1):
    if i==2 or i==3:
        print(i,' is prime')
    elif i==1:
        print(i, 'is not prime')
    elif i%2 == 0 or i%3 == 0:
        print(i,' is not prime')
    else:
        print(i,' is prime')
