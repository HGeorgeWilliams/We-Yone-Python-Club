import math

a=float(input("Enter the value of coefficient, a: "))  # Get inputs for the coefficients of the quadratic equation
b=float(input("Enter the value of coefficient, b: "))
c=float(input("Enter the value of coefficient, c: "))
d=math.pow(b,2)-4*a*c   # Evaluate the condition b^2 - 4*a*c
if d==0:                                # Case 1 : b^2 - 4*a*c = 0
    print("REAL & EQUAL ROOTS")
    x1=-b/(2*a)
    x2=x1
    print(f'x1 = {x1} and x2 = {x2}')
elif d<0:                               # Case 2 : b^2 - 4*a*c < 0
    print("COMPLEX & DISTINCT ROOTS")
    x1r = (-b / (2 * a))
    x1i=(math.sqrt(abs(math.pow(b , 2) - 4 * a * c)) / (2 * a))
    #print(f'x1 = {x1r} + j{x1i} and x2 = {x1r} - j{x1i}')              # using strings to create comlex number output
    print(f'x1 = {complex(x1r,x1i)} and x2 = {complex(x1r,-x1i)}')      # using the Python built-in function
else:                                   # Case 3 : b^2 - 4*a*c > 0
    print("REAL & DISTINCT ROOTS")
    x1 = (-b / (2 * a)) + (math.sqrt(math.pow(b , 2) - 4 * a * c)/ (2 * a))
    x2 = (-b / (2 * a)) - (math.sqrt(math.pow(b , 2) - 4 * a * c) / (2 * a))
    print(f'x1 = {x1} and x2 = {x2}')