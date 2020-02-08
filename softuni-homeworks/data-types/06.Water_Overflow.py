#You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water, 
# which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!"
#  and continue reading the next line. On the last line, print the liters in the tank.
#Constraints
#•	n will be in the interval [1…20]
#•	liters will be in the interval [1…1000]

n=int(input())
capacity=255

for i in range(n):
    liter=int(input())

    if capacity-liter<0:
        print("Insufficient capacity!")
    else:
        capacity-=liter 


print(255-capacity)        

       
