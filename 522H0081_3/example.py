'''Mr. Smith has two children, including at least one son. What is the probability
of both children is boys?

The above problem can be expressed through probability theory with the fol-
lowing conditions: Let Ω = {BB, BG, GB, GG} is the probability space of

gender of Mr. Smith's two children, in which B is male and G is female. What is
the probability of Mr. Smith's two children being boys under the condition that at
least one child is a son?
To solve the above problem, we call:
• A is the event that Mr. Smith's two children to be boys.
• B is the event that at least one of Mr. Smith's children is a boy.
So we need to calculate P (A|B). According to (1) we need to specify P(A∩B)
and P (B).'''


'''The probability of an event , given a sample space of
equiprobable outcomes.'''


from fractions import Fraction
def P(event , space):
    return Fraction(len(event & space), len(space))

S = {'BB', 'BG', 'GB', 'GG'}

B = {s for s in S if 'B' in s}
A_B = {s for s in B if s.count('B')==2}

P_B = P(B, S)
P_A_B = P(A_B, S)
P_A_with_B = P_A_B/P_B

print("Giá trị xác suất P_A_with_B.:",P_A_with_B)