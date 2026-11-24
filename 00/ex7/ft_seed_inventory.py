# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/11 15:50:53 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/11 15:50:54 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit in ('packets', 'grams'):
        if (unit == 'packets'):
            print(seed_type, "seeds:", quantity, unit, "available")
        elif (unit == 'grams'):
            print(seed_type, "seeds:", quantity, unit, "total")
    elif (unit == 'area'):
        print(seed_type, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
