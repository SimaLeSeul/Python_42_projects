# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/12 16:07:43 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/12 16:07:44 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    name: str
    _height: float
    _age: int
    _growth_rate: float

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self._height = height if self._is_valid(height, "height") else 0.0
        self._age = age if self._is_valid(age, "age") else 0
        self._growth_rate = growth_rate

    def _is_valid(self, value: float, field: str) -> bool:
        if value < 0:
            print(f"{self.name}: Error, {field} can't be negative")
            return False
        return True

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self, days: int = 1) -> None:
        self._age += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if not self._is_valid(height, "height"):
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if not self._is_valid(age, "age"):
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-3)
    print()
    print("Current state: ", end="")
    rose.show()
