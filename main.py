from digital_twin.components.localizer import Localizer
from digital_twin.telemetry.logger import TelemetryLogger

localizer = Localizer()

logger = TelemetryLogger()

for minute in range(100):

    localizer.update()

    state = localizer.get_state()

    logger.log(state)

    print(
        f"Minute {state['time']} | "
        f"RF Power: {state['amplifier']['rf_power']} dBm | "
        f"Fan Health: {state['fan']['health']}%"
    )

print("\nSimulation Complete!")
print("Telemetry saved to data/localizer_telemetry.csv")