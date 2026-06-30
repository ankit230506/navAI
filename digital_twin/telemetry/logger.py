import csv
import os


class TelemetryLogger:
    """
    Logs Digital Twin telemetry into a CSV file.
    """

    def __init__(self, filename="data/localizer_telemetry.csv"):

        self.filename = filename

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if not os.path.exists(filename):

            with open(filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Time",
                    "Temperature",
                    "Humidity",
                    "FanHealth",
                    "FanRPM",
                    "AmpHealth",
                    "AmpTemperature",
                    "Efficiency",
                    "RFPower"
                ])

    def log(self, state):

        env = state["environment"]

        fan = state["fan"]

        amp = state["amplifier"]

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                state["time"],
                env["temperature"],
                env["humidity"],
                fan["health"],
                round(fan["rpm"], 2),
                amp["health"],
                amp["temperature"],
                amp["efficiency"],
                amp["rf_power"]
            ])