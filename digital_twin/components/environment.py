import random


class Environment:

    def __init__(self):

        self.temperature = 30.0

        self.humidity = 45.0

        self.wind_speed = 5.0

    def update(self):

        self.temperature += random.uniform(-0.3, 0.3)

        self.humidity += random.uniform(-1, 1)

        self.wind_speed += random.uniform(-0.2, 0.2)

    def get_state(self):

        return {

            "temperature": round(self.temperature, 2),

            "humidity": round(self.humidity, 2),

            "wind_speed": round(self.wind_speed, 2)

        }