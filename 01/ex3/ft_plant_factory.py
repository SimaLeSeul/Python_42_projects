# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/12 15:56:03 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/12 15:56:04 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    name: str
    height: float
    days: int
    growth_rate: float

    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self, days: int = 1) -> None:
        self.days += days


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 0.2),
        Plant("Cactus", 5.0, 90, 0.1),
        Plant("Sunflower", 80.0, 45, 3.0),
        Plant("Fern", 15.0, 120, 0.5),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
