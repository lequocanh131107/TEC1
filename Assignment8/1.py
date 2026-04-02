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


h = Elevator(1, 10)

target = int(input("Enter floor: "))

h.go_to_floor(target)
h.go_to_floor(h.lowest)