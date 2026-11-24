# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/10 01:26:56 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/10 01:26:57 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
