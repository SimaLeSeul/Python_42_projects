# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/25 16:47:54 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/25 16:47:54 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    tests: list[tuple[str, list[str]]] = [
        ("valid", ["Tomato", "Lettuce", "Carrots"]),
        ("invalid", ["Tomato", "lettuce", "Carrots"]),
    ]
    for label, plants in tests:
        print()
        print(f"Testing {label} plants...")
        print("Opening watering system")
        try:
            for plant_name in plants:
                water_plant(plant_name)
        except PlantError as error:
            print(f"Caught PlantError: {error}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
