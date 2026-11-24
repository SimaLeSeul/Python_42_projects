# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/10 01:23:22 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/10 01:23:23 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
