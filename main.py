from digital_twin.components.localizer import Localizer

localizer = Localizer()

for minute in range(20):

    localizer.update()

    state = localizer.get_state()

    print("=" * 60)
    print(f"Simulation Minute : {state['time']}")

    print("\nEnvironment")
    print(state["environment"])

    print("\nCooling Fan")
    print(state["fan"])

    print("\nRF Amplifier")
    print(state["amplifier"])