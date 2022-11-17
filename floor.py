import random
floor=100
def mysteryfloor(floor):
    mystfloor =random.randint(1,100)
    for i in range(1,floor+1):
        if i == mystfloor:
            print(f"Our Mystry floor is {i} this")
    
    


print(mysteryfloor(floor))
