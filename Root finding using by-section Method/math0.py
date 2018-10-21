import math

result = 420

# selection of approximate root a,b
def  eqn(x):
    return (math.pow(x, 3))-4*x - 9

for i in range(-4,4):
   
    #print(" "+ str(i) +" = "+ str(eqn(i)))

	if( i < 0) :
		print(" "+ str(i) +" = "+ str(eqn(i)))
	else:
		print("  "+ str(i) +" = "+ str(eqn(i)))
		
print("Enter the value of a")
a=int(input())

print("Enter the value of b")
b=int(input())
    
#Finding root
while( result != 0.00 ) :
    x=(a+b) / 2
    rootChk = (math.pow(x, 3))-4*x - 9
    result=rootChk
    print("(",a,"+",b,")/2 = " , x, "  f(x) = ",rootChk)
    if (result== 0.00):
        break
    elif( result > 0 ):
                a=x
    else :
            b=x
	
	
print("Answer is :" ,x)

	
