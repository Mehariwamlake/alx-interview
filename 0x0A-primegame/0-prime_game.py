#!/usr/bin/python3

def isWinner(x, nums):
    '''
    Returns the name of the winner
    '''
    winner = []
    for num in nums:
        winner.append(roundWinner(x, num))
    if winner.count('Ben') > (len(winner)/2):
        return 'Ben'
    return 'Maria'


def roundWinner(x, num):
    '''
    Calculates who wons every round
    '''
    if num == 1:
        return 'Ben'
    if num == 2:
        return 'Maria'
    prime_numbers = 1
    for n in range(3, num + 1):
        i = 1
        not_prime = 0
        while (n - i) >= 2:
            if n % (n - i) == 0:
                not_prime += 1
            i += 1
        if not_prime == 0:
            prime_numbers += 1
    if prime_numbers % 2 == 0:
        return 'Ben'
    return 'Maria'