from digital_twin.components.environment import Environment
from digital_twin.components.fan import CoolingFan
from digital_twin.components.amplifier import RFAmplifier


class Localizer:
    """
    Digital Twin of an Airport Localizer.
    """

    def __init__(self):

        self.environment = Environment()

        self.fan = CoolingFan()

        self.amplifier = RFAmplifier(
            self.fan,
            self.environment
        )

        self.time = 0

    def update(self):

        self.time += 1

        self.environment.update()

        self.fan.update()

        self.amplifier.update()

    def get_state(self):

        return {

            "time": self.time,

            "environment": self.environment.get_state(),

            "fan": self.fan.get_state(),

            "amplifier": self.amplifier.get_state()

        }