# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_errors.py                                :+:      :+:    :+:   #
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


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(self, message)


def check_plant(plant_name: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")
    print(f"The {plant_name} plant is healthy")


def check_water(water_level: int, water_needed: int) -> None:
    if water_level < water_needed:
        raise WaterError("Not enough water in the tank!")
    print("Water tank level is fine")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        check_water(5, 10)
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        check_water(5, 10)
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_plant_error()
    print()
    test_water_error()
    print()
    test_garden_errors()
    print()
    print("All custom error types work correctly!")
