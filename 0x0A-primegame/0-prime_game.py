#!/usr/bin/python3

"""
prime game
"""

def isWinner(x, nums):
    winner = []
    for num in nums:
        winner.append(roundWinner(x, num))
    if winner.count('Ben') > (len(winner)/2):
        return 'Ben'
    return "Maria"
    """
    cakcuates who win
    """


def roundWinner(x, num):
    if num == 1:
        return 'Ben'
    if nums == 2:
        return 'Maria'
    prime_num = 1
    for n in range(3, num + 1):
        i = 1
        not_prime = 0
        while (n - 1) >= 2:
            if n% (n -i) == 0:
                not_prime += 1
            i += 1
        if not_prime == 0:
            prime_num += 1
    if prime_num % 2 == 0:
        return 'Ben'
    return 'Maria'