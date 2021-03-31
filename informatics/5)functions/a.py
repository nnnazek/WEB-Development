def min(a, b, c, d):
    min1 =  0;
    for i in range(0,5):
        if( a <= b and a <= c and a <= d):
            min1 = a;
        
        elif( b <= a and b <= c and b <= d):
            min1 = b;
        
        elif( c <= a and c <= b and c <= d):
            min1 = c;
        
        elif( d <= a and d <= b and d <= c):
            min1 = d;
        
    
    return min1;
# funtion helps us to input 2 or more integers(or something els) in one line of input
a, b, c, d = map(int, input().split()) 



print(min(a, b, c, d))