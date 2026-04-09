class Elevator:

    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def go_to_floor(self, des_floor):
        start = self.current
        stop = des_floor

    for i in range(start, stop):
        self.floor_up()

    while(self.current > self.bottom):
        self.floor_down()

    def floor_up(self):
        self.current += 1
        print(self.current)

    def floor_down(self):
        self.current -= 1
        print (self.current)

h = Elevator(1, 10)
h.go_to_floor(5)