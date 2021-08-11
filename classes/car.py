# Car class

# maximum speed
# keep track of current speed = use a _
# Getter - return the current speed
# Accelerate and Decelerate methods - add speed or takeaway
# speed to the car

# accelerate past the cars max speed
# what happens if you keep braking?


class Car:
    def __init__(self, max_speed, speed=0):
        self.max_speed = max_speed
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed


c = Car(150)
c.accelerate()
c.brake()
print(c.get_speed())



# c = Car.max_speed(180)
# c.accelerate(50)
# c.decelerate(10)
# print(c.get_speed())



