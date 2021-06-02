def rectangle_area(a,b):
    area = a*b
    print(f'area of rectangle => {area}')
rectangle_area(2,3)


def perimeter(a,b):
    perimeter = 2*(a+b)
    print(f'perimeter of recangle ==> {perimeter}')
perimeter(4,5)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def area_circle(r):
    area = 3.14*r**2
    print(f'area of circle => {area}')
area_circle(4)

def circumference(r):
    circumference = 2*3.14*r
    print(f'circumference of circle :: {circumference}')
circumference(3)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def vote_eligibility(age):
    if age >= 18:
        print('wow,you can vote')
    else:
        print('sorry,u r not eligible')
vote_eligibility(14)
vote_eligibility(24)

##############################################################
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f=f*i
    print('factorial of',n,'is',f)
    return f
factorial(5)

fact ={}
print('factorial of number from 1 to 10')
for i in range(1,10):
    m=factorial(i)
    fact[i]=m
print(fact)



    