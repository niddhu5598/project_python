def get_speed(dis,time):
    speed = dis / time
    print(f'the speed is {speed}')

# calling
get_speed(50,5)

distance = 400
time = 25
get_speed(distance,time)

get_speed(dis=250,time=10)



def pythagoras(perpendicular:int,base:int):
    hyp = (perpendicular**2+base**2)**0.5
    print(f'p={perpendicular}, b={base},h={hyp}')
pythagoras(3,4)