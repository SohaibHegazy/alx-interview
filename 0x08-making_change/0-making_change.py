#!/usr/bin/python3
'''
determine the fewest number of coins needed to
meet a given amount
'''


def makeChange(coins, total):
    '''
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.

    coins: list of the values of the coins in your possession
    total: the number to be met.

    if total is 0 or less return 0
    if total can't be met return -1
    '''

    if total <= 0:
        return 0

    temp_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        result = (total - temp_total) // coin
        temp_total += result * coin
        used_coins += result
        if temp_total == total:
            return used_coins
    return -1
