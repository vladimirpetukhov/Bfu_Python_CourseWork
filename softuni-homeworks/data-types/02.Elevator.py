#Calculate how many courses will be needed to elevate n persons by using an elevator 
# of capacity of p persons. The input holds two lines: the number of people n 
# and the capacity p of the elevator.
import math

people=int(input())
capacity=int(input())

print(math.ceil(people/capacity))