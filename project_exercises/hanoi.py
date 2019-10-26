<<<<<<< HEAD
def result_hanoi(disks, origin, middle, destination):
    if disks >= 1:
        #Una función recursiva se llama a sí misma
        result_hanoi(disks-1, origin, destination, middle)
        print("Move disk from tower: ", origin, "to tower: ", destination)
        result_hanoi(disks-1, middle, origin, destination)
=======
def result_hanoi(disks, origin, middle, destination):
    if disks >= 1:
        #Una función recursiva se llama a sí misma
        result_hanoi(disks-1, origin, destination, middle)
        print("Move disk from tower: ", origin, "to tower: ", destination)
        result_hanoi(disks-1, middle, origin, destination)
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
result_hanoi(3,1,2,3)