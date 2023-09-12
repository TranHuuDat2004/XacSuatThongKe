# Define function P

from fractions import Fraction

'''The probability of an event , given a sample space of
equiprobable outcomes.'''

def P(event , space):
    return Fraction(len(event & space), len(space))

D = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6}

print("Ket qua la =",P(even, D))