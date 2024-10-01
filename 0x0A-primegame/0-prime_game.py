#!/usr/bin/python3
'''
The Prime Game
'''


def isWinner(x, nums):
    '''
    The function to determine the winner
    '''
    def sieve_of_eratosthenes(n):
        '''
        Helper function to find prime numbers up to a given number n
        '''
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p] == True:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        prime_list = []
        for p in range(2, n + 1):
            if primes[p]:
                prime_list.append(p)
        return prime_list

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        primes = sieve_of_eratosthenes(n)
        prime_turns = len(primes)
        
        if prime_turns % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

