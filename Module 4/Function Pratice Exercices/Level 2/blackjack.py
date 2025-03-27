# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

from random import randint

def blackjack(card1, card2, card3):
    if not (1 <= card1 <= 11 and 1 <= card2 <= 11 and 1 <= card3 <= 11):
        return 'BUST'
    
    total = card1 + card2 + card3

    if total <= 21:
        return total

    if total > 21 and (card1 == 11 or card2 == 11 or card3 == 11):
        total -= 10
        return total if total <= 21 else 'BUST'
    return 'BUST'

print(blackjack(randint(1, 11), randint(1, 11), randint(1, 11)))
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))