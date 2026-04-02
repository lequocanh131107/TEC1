class Elevator:

    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.current = lowest

    def floor_up(self):
        if self.current < self.highest:
            self.current += 1
        print("Current floor:", self.current)

    def floor_down(self):
        if self.current > self.lowest:
            self.current -= 1
        print("Current floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


class Building:

    def __init__(self, lowest, highest, number):
        self.elevators = []

        for i in range(number):
            self.elevators.append(Elevator(lowest, highest))

    def run_elevator(self, num, floor):
        self.elevators[num].go_to_floor(floor)


b = Building(1, 10, 3)

b.run_elevator(0, 6)