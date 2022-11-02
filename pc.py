
import random


class Thing:

    def __init__(self, weight: float, value: float) -> None:
        self.weight = weight
        self.value = value


def fits(capacity: int, objects: list[Thing], threshold: int) -> bool:

    # sum of objects weight <= capacity
    # sum of objects value >= threshold


    return False



def knapsackGreProc(self, W, V, M, n):
    packs = []
    for i in range(n): 
        packs.append(KnapsackPackage(W[i], V[i]))
    packs.sort(reverse = True)
    
    remain = M
    result = 0
    i = 0
    stopProc = False
    while (stopProc != True):
        if (packs[i].weight <= remain):
            remain -= packs[i].weight;
            result += packs[i].value;
        print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)
        if (packs[i].weight > remain):
            i += 1
        if (i == n):
            stopProc = True
    print("Max Value:\t", result)



if __name__ == "__main__":
    capacity = 100
    threshold = 50

    things: list[Thing] = []
    for i in range(100):
        things.append(Thing(random.randint(0, 10), i))

    print("backpack {", "capacity", "=>", capacity, "things", "=>", things "}")
    print("fits", "=>", fits(capacity, things, threshold))
