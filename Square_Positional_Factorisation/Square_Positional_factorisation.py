import math

num = input('Insert ODD !! (3,5,7..23, etc) number to factorise:\n')
num = int(num)
num_sqrt=math.sqrt(num)     # square root
column=math.ceil(num_sqrt)  # round up
col_sq=column^2             # creating perfect square

# Odd Numbers and their parabola images, are divided between two types of columns
# First we must check where we are.  Nearly all code is the same for column types,
# But when  we check ' if d2+num_dist == ' for wrong column we dont get a andswer,
# For optimalisation code this  problem should be included 

if  column%2==0 :  # Odd numbers a
    print('yes')
    num_dist=(col_sq-num+1)/2
    end_div = column - 1     
    
else: 
    print('no')
    num_dist=(col_sq-num)/2
    end_div = column

full_triplet = math.ceil(((end_div + 1)/6))    #  ex. 7.33->8,  7.66-> 8, 8 -> 8
triplet_type=((end_div + 1)/6)-(full_triplet-1)  # ex.  7.33-(8-1)= 0.33
range_div =(full_triplet - 1)*2     # Range between end divisor and starting divisor

start_div=end_div-range_div  # Starting divisor for dv2

# start_div/end_div  # going to 0.65 and  1.5..  4/2.6..
# end_div/start_div
  
# Calculating quartets parameters for 3 cursors (3 starting points)
d1_quart_type=((start_div+1-2)/(4*2))  # ex. 3.25, 3.50, 3.75, 4.0   4 possible ranges 
d1_quart = math.ceil(d1_quart_type)

d2_quart_type=((start_div+1)/(4*2))
d2_quart= math.ceil(d2_quart_type)

d3_quart_type=((start_div+1+2)/(4*2))
d3_quart= math.ceil(d2_quart_type)

d1_type=d1_quart_type - math.floor(d1_quart_type)  # only 4 types of numbers 0.25, 0.5, 0.75 0.00
d2_type=d2_quart_type - math.floor(d2_quart_type)
d3_type=d2_quart_type - math.floor(d3_quart_type)

if (d1_type == 0.25):  # choosing starting points for d1 depending on  quartet
    d1_start=1         # repeated 3 times for 3 cursors
    d1_div=1
elif (d1_type == 0.5):
    d1_start=2
    d1_div=3
elif (d1_type == 0.75):
    d1_start=4
    d1_div=5
elif (d1_type == 0):
    d1_start=7
    d1_div=7
    
if (d2_type == 0.25):
    d2_start=1
    d2_div=1
elif (d2_type == 0.5):
    d2_start=2
    d2_div=3
elif (d2_type == 0.75):
    d2_start=4
    d2_div=5
elif (d2_type == 0):
    d2_start=7
    d2_div=7

if (d3_type == 0.25):
    d3_start=1
    d3_div=1
elif (d3_type == 0.5):
    d3_start=2
    d3_div=3
elif (d3_type == 0.75):
    d3_start=4
    d3_div=5
elif (d3_type == 0): 
    d3_start=7
    d3_div=7


# Calculating vertex position in each Cursor
# Note: Divisors are creating easy to calculate parabolas. We always starting from Vertex

d1=d1_start+((d1_quart-1)*d1_div)    # Cursor 1 Setup
dv1=start_div-2                            

d2=d2_start+((d2_quart-1)*d2_div)    # Cursos 2 Setup
dv2=start_div                         

d3=d3_start+((d3_quart-1)*d3_div)   # Cursor 3 Setup
dv3=start_div+2                          


# Cursors triplet offset calculating. Because of parabola relation,
#  there is only 3 types of offsets to start. Our Focus  is Cursor 2
# But we need to know all 3 Cursores

if (0.2 < triplet_type < 0.4):  # 0.33
    of_d1=1
    of_d2=3
    of_d3=6
    t=1
elif (0.5 < triplet_type < 0.7):  # 0.66
    of_d1=3
    of_d2=6
    of_d3=10
    t=2
elif (triplet_type==0) or ( -0.1< triplet_type < 0.1) or (triplet_type == 1): # 0.00
    of_d1=0
    of_d2=1
    of_d3=3
    t=3
   
d1=d1-of_d1
d2=d2-of_d2
d2=d3-of_d3

####

## Step 0   Starting point ##
## Variables below can be comented, it is only reminder
d1=d1           # Only integer Number
dv1=dv1         # start_div -2
d2=d2
dv2=dv2         # start_div
d3=d3
dv3=dv3         # start_div +2
t=t             # possible values 1,2,3

###
# WORKING ENGINE
###

# +1 parameter in range_div is option we should finish much ealier
# It is a rough code, for calculating big numbers p,q in RSA type. p*q=n
# end_div is a range of sqrt(n), start_div is around 0.65*end_div
# Rought calculation using known RSA numbers, showed that smaller divisor p
# is very close to divisor parabola vertex, with gives a oportunity to fast calculations
# This code cover only one number path, but seems to be usefull, as I said ealier.

# In code can be error so please check, it is alpha stage. Not tested. Only workable idea presented.
# Code is open source. And for racing computations, should be optimzed.

# It is simple "shift register", looped when ouf of range <0, But only possible to create
# when you understand Square Positional System

## How it is possible ? 
# Because Square Positional System uses two parametes for each number
# Column where number is placed,  and distance between Square axis (perfect square) and number
# And of course similarity and scalability of each divisor parabola, So computating 'starting point' 
# is very easy

# If you find error please give me a hint


for n in range(range_div+1): # n start from 0 ,  

    d1=d2-((2*t-1)+n*6)   
    if d1<0:
        d1=dv1+d1
    d2=d3-((2*t+1)+n*6)

    if d2<0:
        d2=dv2+d1

    d3=(d2-d1)+d2
    if d3<0:
        d3=(d2-(d1-dv1))+d2

    if d2+num_dist==dv2+1:     # only works for Odd numbers columns  9,11,13...
        print('divisor', dv2,'factorisation finished')  # Find numers in 1.0 full divisor period (close to quare axis) BOTTOM
    ####
    if d2+num_dist==(dv2+3)/2:   # only works for Even numbers colums  6,10,12...
        print('divisor', dv2,'factorisation finished')  # Find numers in 0.5 half divisor period (close to quare axis) TOP
    if d2+num_dist==(((dv2-1)/2)+1)+(dv2+1):   # only works for Even numbers colums  6,10,12...
        print('divisor', dv2,'factorisation finished')   #  Find numers in 1.5 full and half divisor period  TOP

    dv1=dv1+1
    dv2=dv2+1
    dv3=dv3+1

    


