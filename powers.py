def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a==b:
        result=a
        return result
    elif a<b:
        while a>0:
           result=a-1
           if a%result==0:
               if a%result==0 and b%result==0:
                   print result
           else: 
               result=result-1
                   
    elif b<a:
        while b>0:
           result=b-1
           if b%result==0:
               if a%result==0 and b%result==0:
                   print result
           else:
               result-=1
    
           