import math  as m
def function(a,b):
    sqr_a=float(m.sqrt(a))
    sqr_b=float(m.sqrt(b))
    
    while int(sqr_a+.8)**2!=a and a<b:
        a=a+1
        sqr_a=float(m.sqrt(a))
    while int(sqr_b+.8)**2!=b and b>a:
        b=b-1
        sqr_b=float(m.sqrt(b))
    if int(sqr_a+.8)**2!=a or int(sqr_b+.8)**2!=b:
        return 0
    else:
        return sqr_b-sqr_a+1



if __name__ == "__main__":
    a=3
    b=9
    print(function(a,b))