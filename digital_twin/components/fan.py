from digital_twin.core.component import Component


class CoolingFan(Component):

    def __init__(self):

        super().__init__(

            component_id="FAN001",

            name="Cooling Fan"

        )

        self.rpm = 3000

    def update(self):

        self.age += 1

        self.degrade(0.01)

        self.calculate_health()

        self.rpm = 3000 * (self.health / 100)
    def get_state(self):
        state = super().get_state()
        state["rpm"] = round(self.rpm, 2)
        return state