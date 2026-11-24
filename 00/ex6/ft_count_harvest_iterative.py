# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/10 01:33:07 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/10 01:33:08 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))
    days = 1
    while (days <= n):
        print("Day", days)
        days = days + 1
    print("Harvest time!")
