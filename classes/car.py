# Car class

# maximum speed
# keep track of current speed = use a _
# Getter - return the current speed
# Accelerate and Decelerate methods - add speed or takeaway
# speed to the car

# accelerate past the cars max speed
# what happens if you keep braking?


class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0

    def get_speed(self):
        return self.speed

    def accelerate(self, accelerate):
        self.speed += accelerate

    def decelerate(self, decelerate):
        self.speed -= decelerate


c = Car(0)
c.accelerate(20)
c.decelerate(20)
print(c.get_speed())





# print(c.get_speed())


