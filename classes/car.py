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
        self._speed = 0

    def get_speed(self):
        return self._speed

    def accelerate(self, speed_increase):
        new_speed = self._speed + speed_increase
        self._speed = min(self.max_speed, new_speed)

    def brake(self, speed_decrease):
        self._speed = max(0, self._speed - speed_decrease)


c = Car(180)
c.accelerate(40)
c.accelerate(20)
c.brake(10)
print(c.get_speed())

# car is the max speed it wont go over that or below 0


