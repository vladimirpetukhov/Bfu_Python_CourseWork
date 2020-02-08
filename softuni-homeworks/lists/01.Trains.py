# You will receive how many wagons the train has. Create a list with that length with all zeros. Until you
# receive the command &quot;End&quot;, you get some of the following commands:
# add {people} -&gt; adds the people in the last wagon
# insert {index} {people} -&gt; adds the people at the given wagon
# leave {index} {people} -&gt; removes the people from the wagon
# After you receive the &quot;End&quot; command print the train

wagons_count = int(input())
wagons = [0]*wagons_count

while True:
    command = input().split(' ')

    if command[0] == 'End':
        break
    elif command[0] == 'add':
        wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        index = command[1]
        people = command[2]
        wagons[index] += people
    elif command[0] == 'leave':
        index = command[1]
        people = command[2]
        wagons[index] -= people


print(wagons)
