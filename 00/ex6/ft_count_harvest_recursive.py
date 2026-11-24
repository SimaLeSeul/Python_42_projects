# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mibaboul <mibaboul@student.42angouleme.    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/11/10 01:38:36 by mibaboul          #+#    #+#             #
#    Updated: 2026/11/10 01:38:37 by mibaboul         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def recursive(days, n):
    if (days > n):
        return
    print("Day", days)
    days = days + 1
    recursive(days, n)


def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    days = 1
    recursive(days, n)
    print("Harvest time!")
