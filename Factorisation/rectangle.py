import math

num = input('Input Column integer number \n')
num = int(num)
square=num**2
border=square-((num-1)*2)

#  "Column Upper Side , Half cycle"
print('\nColumn Upper side, Half parabola cycle \nSquare: ',square,'\n')
k=1     # inital Paramteres
m=1
dif=1
rect=square

while (border-1)<rect:
    for n in range(num):
        rect=square-k 
        d1=num-dif
        d2=num+dif
        test=d1*d2
        if (border-1)<rect:
            print('Rectangle: ',rect, 'have 2 divisors: ',d1, 'and',d2, 'Distance: ',k, 'Test: ' ,test,)
        k=k+(8*m)       # Distance calculation
        dif=dif+2
        m=m+1  

# Column Lower Side , Full Cycle"
print('\nColumn Lower side, Full parabola cycle \nSquare: ',square,'\n')
k=4     # initial Parameters
m=1
dif=2
rect=square

while border<rect:
    for n in range(num):
        rect=square-k 
        d1=num-dif
        d2=num+dif
        test=d1*d2
        if border<rect:
            print('Rectangle: ',rect, 'have 2 divisors: ',d1, 'and',d2, 'Distance: ',k, 'Test: ' ,test,)
        k=k+(8*m)+4     # Distance calculation
        dif=dif+2
        m=m+1 