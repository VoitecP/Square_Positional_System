import math
print('This program find divisors N number from range 0.7sqrt(N) -> sqrt(N), usefull for BIG odd numbers')
print('Program starts from around 0.7sqrt(N), from divisor parabola vertex,')
num = input('Insert only ODD  (1887, 2479 etc. ) number to factorise:\n')
num = int(num)
num_sqrt=math.sqrt(num)     # square root
column=math.ceil(num_sqrt)  # round up
col_sq=column**2             # creating perfect square
#col_mod=3       # variable declaration

print(col_sq)
# Column odd/even checker
if  column%2==0:
    col_mod=0
elif column%2==1: 
    col_mod=1

# Calculating colum type for odd Numbers
if  col_mod==0:  # Even Column numbers   2, 4,6 .. 44
    num_place=(col_sq-num+1)/2
    end_div = column - 1     
    
elif col_mod==1: # # Odd Column numbers   3,5,7.. 45
    num_place=(col_sq-num)/2
    end_div = column


# Triplet calculation for c2 Cursor 2 divisor position
triplet=(end_div + 1)/6
triplets = math.ceil(triplet)                # Quantity of full triplets
triplet_type=triplet-(triplets-1)            # Triplet type values: 0.33, 0.66, 1.00

# Calculating Starting divisor for c2 cursor 2 divisor position
# kol 27  moze zależna
range_div =(triplets - 1)*2
steps_div=triplets-1            # it will be ok -1 no much difference when -0
#range_div=triplets
start_div=end_div-range_div                  # Starting divisor for c2 

# Quartet calculation for c2 Cursor 2 value
c2_quartet=((start_div+1)/8)            
c2_quartets= math.ceil(c2_quartet)           # Qauantity of full quartets
c2_quartet_type=c2_quartet-(c2_quartets-1)           # Quartet type value:   0.25, 0.50, 0.75, 1.00 

# Quartet calculation for c3 Cursor 3 value
c3_quartet=((start_div+2+1)/8)            
c3_quartets= math.ceil(c3_quartet)           # Qauantity of full quartets
c3_quartet_type=c3_quartet-(c3_quartets-1)           # Quartet type value:   0.25, 0.50, 0.75, 1.00 


# Matching Cursors value offest depend of triplet type , and column type
if  col_mod==0:            # Ex.  Col 44 div_start
    if (0.2 < triplet_type < 0.4):               # 0.33
        of1_c2=0            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=0 
        of2_c2=1            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=3
    elif (0.5 < triplet_type < 0.7):              # 0.66
        of1_c2=0            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=1 
        of2_c2=3            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=5
    elif (triplet_type == 1):                      # 1.00           
        of1_c2=1            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=3 
        of2_c2=5            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=7

elif col_mod==1:
    if (0.2 < triplet_type < 0.4):               # 0.33
        of1_c2=0            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=1 
        of2_c2=3            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=5
    elif (0.5 < triplet_type < 0.7):              # 0.66
        of1_c2=1            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=3 
        of2_c2=5            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=7
    elif (triplet_type == 1.0):                     # 1.00           
        of1_c2=3            # Initial offsets for Cursor 2 and Cursor 3
        of1_c3=6 
        of2_c2=7            # Continous offsets for Cursor 2 and Cursor 3
        of2_c3=9                    # add 2 everywhere , comparing to of2_c3 = 7

# Matching Cursor 2 Initial parameterer dependent of quartet type
if (c2_quartet_type == 0.25):  
    c2_starter=1         
    c2_counter=1
elif (c2_quartet_type == 0.5):
    c2_starter=2
    c2_counter=3
elif (c2_quartet_type == 0.75):
    c2_starter=4
    c2_counter=5
elif (c2_quartet_type == 1):
    c2_starter=7
    c2_counter=7

# Matching Cursor 3 Initial parameterer dependent of quartet type
if (c3_quartet_type == 0.25):  
    c3_starter=1         
    c3_counter=1
elif (c3_quartet_type == 0.5):
    c3_starter=2
    c3_counter=3
elif (c3_quartet_type == 0.75):
    c3_starter=4
    c3_counter=5
elif (c3_quartet_type == 1):
    c3_starter=7
    c3_counter=7

# Calculating  Parabola Vertex for Crusor Cursor 2 and Cursor 3
c2=c2_starter+((c2_quartets-1)*c2_counter)    # Cursor 2 For loop setup                          
c3=c3_starter+((c3_quartets-1)*c3_counter)    # Cursos 3 For loop Setup

# Including initial offset value for Cursor 2 and Cursor 3
c2=c2-of1_c2
c3=c3-of1_c3

#### Working Engine
print('col_mod',col_mod)
if  col_mod==0: 

    dv1=start_div-2
    dv2=start_div
    dv3=start_div+2
    half1_dv2=(dv2+1)/2      #  for 1.5 cycle , if number is places in 1.5 divisor cycle
    half2_dv2=(dv2-1)/2      #  for 0.5 cycle , if number is places in 0.5 divisor cycle

    if  ((end_div-1))/2<num_place:      # Posibility to optimalisation
        print('Number is in 1.5 divisor cycle, not in 0.5 divisor cycle')  


    for n in range(steps_div):   #  n should start from 0  !
        print('for n',n)
        c1=c2-(of2_c2+(n*6))
        if c1<=0:               # need loop if<0      
            c1=dv2+c1
            print('if<0 c1',c1)     
        c2=c3-(of2_c3+(n*6))
        if c2<=0:
            c2=dv3+c2
            print('if<0 c2',c2)  
        c3=(c2-c1)+c2
        if (dv3+2)<c3:                   # obliczone juz na nowy parametr trzeba na stare parametry.
            c3=c3-dv2                   #  or  value: dv3-2, works both dv2, dv3-2 
            print('if<0 c3',c3)  
        dv1=dv1+2
        dv2=dv2+2
        dv3=dv3+2

        half1_dv2=half1_dv2+1 
        half2_dv2=half2_dv2+1
        
        # if number is places in 1.5 divisor cycle
        if c2+num_place-half1_dv2 == dv2+1:
            print('Divisor: ', dv2,'Factorisation finished in ',n+1, 'steps, c2 parameter ',c2)
        # if number is places in 0.5 divisor cycle
        if c2+num_place+half2_dv2 == dv2+1:
            print('Divisor: ', dv2,'Factorisation finished in ',n+1, 'steps, c2 parameter ',c2)
        print('n steps end ',n,'n*6',n*6, ' c1 ',c1, 'c2 ',c2,'c3',c3, 'div2' ,dv2  )

elif col_mod==1:

    dv1=start_div-2
    dv2=start_div
    dv3=start_div+2

    for n in range(steps_div):   #  n should start from 0  !
        print('for n',n)
        c1=c2-(of2_c2+(n*6))
        if c1<=0:               # need loop if<0      
            c1=dv2+c1
            print('if<0 c1',c1)   
        c2=c3-(of2_c3+(n*6))
        if c2<=0:
            c2=dv3+c2
            print('if<0 c2',c2)
        c3=(c2-c1)+c2
        if (dv3+2)<c3:                         # obliczone juz na nowy parametr trzeba na stare parametry.
            c3=c3-dv2           # dv3-2
            print('if<0 c3',c3)
        dv1=dv1+2
        dv2=dv2+2
        dv3=dv3+2

        # full cycle   # wrong statement if should be befor for loop
        
        if c2+num_place == dv2+1:
            print('Divisor: ', dv2,'Factorisation finished in ',n+1, 'steps, c2 parameter ',c2)
        print('n steps end ',n,'n*6',n*6, ' c1 ',c1, 'c2 ',c2,'c3',c3, 'div2' ,dv2  )