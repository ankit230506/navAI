from digital_twin.core.component import Component


class RFAmplifier(Component):
    """
    Digital Twin model of an RF Power Amplifier.
    """

    def __init__(self, fan, environment):

        super().__init__(
            component_id="AMP001",
            name="RF Amplifier"
        )

        self.fan = fan
        self.environment = environment

        self.temperature = 35.0
        self.efficiency = 100.0
        self.rf_power = -41.6

    def update(self):

        self.age += 1

        # Component ageing
        self.degrade(0.005)

        # Temperature depends on fan health and ambient temperature
        self.temperature = (
            self.environment.temperature
            + 5
            + (100 - self.fan.health) * 0.2
        )

        # Efficiency decreases as temperature increases
        self.efficiency = max(70, 100 - (self.temperature - 30) * 0.5)

        # RF Power decreases with efficiency
        self.rf_power = -41.6 - ((100 - self.efficiency) * 0.02)

        self.calculate_health()

    def get_state(self):

        state = super().get_state()

        state.update({

            "temperature": round(self.temperature, 2),

            "efficiency": round(self.efficiency, 2),

            "rf_power": round(self.rf_power, 2)

        })

        return state