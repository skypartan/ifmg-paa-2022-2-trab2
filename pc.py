
import random


class Thing:

    def __init__(self, weight: float, value: float) -> None:
        self.weight = weight
        self.value = value


def fits(capacity: int, objects: list[Thing], threshold: int) -> bool:

    # sum of objects weight <= capacity
    # sum of objects value >= threshold

    remain = capacity
    result = 0

    i = 0
    stopProc = False
    while (stopProc != True):
        if (objects[i].weight <= remain):
            remain -= objects[i].weight
            result += objects[i].value

        print("Pack ", i, " - Weight ", objects[i].weight, " - Value ", objects[i].value)

        if (objects[i].weight > remain):
            i += 1

        if (i == threshold):
        # if result > threshold or i == len(objects):
            stopProc = True

    print("Max Value:\t", result)


    return result >= threshold


if __name__ == "__main__":
    capacity = 100
    threshold = 50

    things: list[Thing] = []
    for i in range(100):
        things.append(Thing(random.randint(1, 10), i))

    print("backpack {", "capacity", "=>", capacity, "}")#, "things", "=>", things, "}")
    print("fits", "=>", fits(capacity, things, threshold))
