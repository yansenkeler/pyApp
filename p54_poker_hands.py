# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
# 1. High Card:        Highest value card.
# 2. One Pair:         Two cards of the same value.
# 3. Two Pairs:        Two different pairs.
# 4. Three of a Kind:  Three cards of the same value.
# 5. Straight:         All cards are consecutive values.
# 6. Flush:            All cards of the same suit.
# 7. Full House:       Three of a kind and a pair.
# 8. Four of a Kind:   Four cards of the same value.
# 9. Straight Flush:   All cards are consecutive values of same suit.
# 10. Royal Flush:      Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the highest value wins; for example,
# a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players
# have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards
# tie then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	 5H 5C 6S 7S KD  2C 3S 8S 8D TD    Player 2
#         Pair of Fives  Pair of Eights
#
# 2	 	 5D 8C 9S JS AC  2C 5C 7D 8S QH    Player 1
#       Highest card Ace Highest card Queen
#
# 3	 	 2D 9C AS AH AC  3D 6D 7D TD QD    Player 2
#          Three Aces    Flush with Diamonds
#
# 4	 	 4D 6S 9H QH QC  3D 6D 7H QD QS    Player 1
#        Pair of Queens  Pair of Queens
#      Highest card Nine Highest card Seven
#
# 5	 	 2H 2D 4C 4D 4S  3C 3D 3S 9S 9D    Player 1
#          Full House       Full House
#       With Three Fours  with Three Threes
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten
# cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?
import time


# def sort_card(cards):
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#     list.sort(cards, key=lambda x: ranks.index(x[0]))
#     return cards


def get_effect_card(cards):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    rank_data = {}
    list.sort(cards, key=lambda x: ranks.index(x[0]))
    values = []
    suits = []
    for card in cards:
        values.append(card[0])
        suits.append(card[1])
    if values[0] == 'T' and values[1] == 'J' and values[2] == 'Q' and values[3] == 'K' and values[4] == 'A' \
            and suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        rank_data['rank'] = 10
    elif ranks.index(values[0])+1 == ranks.index(values[1]) \
            and ranks.index(values[0])+2 == ranks.index(values[2]) \
            and ranks.index(values[0])+3 == ranks.index(values[3]) \
            and ranks.index(values[0])+4 == ranks.index(values[4]) \
            and suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        rank_data['rank'] = 9
        rank_data['value1'] = values[4]
    elif values.count(values[0]) == 1 and values.count(values[4]) == 4:
        rank_data['rank'] = 8
        rank_data['value1'] = values[4]
        rank_data['value2'] = values[0]
    elif values.count(values[0]) == 4 and values.count(values[4]) == 1:
        rank_data['rank'] = 8
        rank_data['value1'] = values[0]
        rank_data['value2'] = values[4]
    elif values.count(values[0]) == 2 and values.count(values[4]) == 3:
        rank_data['rank'] = 7
        rank_data['value1'] = values[4]
        rank_data['value2'] = values[0]
    elif values.count(values[0]) == 3 and values.count(values[4]) == 2:
        rank_data['rank'] = 7
        rank_data['value1'] = values[0]
        rank_data['value2'] = values[4]
    elif suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        rank_data['rank'] = 6
        rank_data['value'] = values
    elif ranks.index(values[0])+1 == ranks.index(values[1]) \
            and ranks.index(values[0])+2 == ranks.index(values[2]) \
            and ranks.index(values[0])+3 == ranks.index(values[3]) \
            and ranks.index(values[0])+4 == ranks.index(values[4]):
        rank_data['rank'] = 5
        rank_data['value1'] = values[4]
    elif values.count(values[0]) == 3:
        rank_data['rank'] = 4
        rank_data['value1'] = values[0]
        rank_data['value2'] = values[3]
        rank_data['value3'] = values[4]
    elif values.count(values[4]) == 3:
        rank_data['rank'] = 4
        rank_data['value1'] = values[4]
        rank_data['value2'] = values[1]
        rank_data['value3'] = values[0]
    elif values.count(values[2]) == 3:
        rank_data['rank'] = 4
        rank_data['value1'] = values[2]
        rank_data['value2'] = values[4]
        rank_data['value3'] = values[0]
    elif values.count(values[0]) == 2 and values.count(values[2]) == 2:
        rank_data['rank'] = 3
        rank_data['value1'] = values[2]
        rank_data['value2'] = values[0]
        rank_data['value3'] = values[4]
    elif values.count(values[4]) == 2 and values.count(values[2]) == 2:
        rank_data['rank'] = 3
        rank_data['value1'] = values[4]
        rank_data['value2'] = values[2]
        rank_data['value3'] = values[0]
    elif values.count(values[0]) == 2 and values.count(values[4]) == 2:
        rank_data['rank'] = 3
        rank_data['value1'] = values[4]
        rank_data['value2'] = values[0]
        rank_data['value3'] = values[2]
    elif values.count(values[0]) == 2:
        rank_data['rank'] = 2
        rank_data['value1'] = values[0]
        rank_data['value2'] = values[4]
        rank_data['value3'] = values[3]
        rank_data['value4'] = values[2]
    elif values.count(values[1]) == 2:
        rank_data['rank'] = 2
        rank_data['value1'] = values[1]
        rank_data['value2'] = values[4]
        rank_data['value3'] = values[3]
        rank_data['value4'] = values[0]
    elif values.count(values[2]) == 2:
        rank_data['rank'] = 2
        rank_data['value1'] = values[2]
        rank_data['value2'] = values[4]
        rank_data['value3'] = values[1]
        rank_data['value4'] = values[0]
    elif values.count(values[3]) == 2:
        rank_data['rank'] = 2
        rank_data['value1'] = values[3]
        rank_data['value2'] = values[2]
        rank_data['value3'] = values[1]
        rank_data['value4'] = values[0]
    else:
        rank_data['rank'] = 1
        rank_data['value'] = values
    return rank_data


def who_win(player1, player2):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    rank_data1 = get_effect_card(player1)
    rank_data2 = get_effect_card(player2)
    if rank_data1['rank'] > rank_data2['rank']:
        return 1
    elif rank_data1['rank'] < rank_data2['rank']:
        return 2
    else:
        if rank_data1['rank'] == 10:
            return 0
        elif rank_data1['rank'] == 9 or rank_data1['rank'] == 5:
            if ranks.index(rank_data1['value1']) > ranks.index(rank_data2['value1']):
                print(p1, rank_data1, '\n', p2, rank_data2, '\n\n')
                return 1
            elif ranks.index(rank_data1['value1']) < ranks.index(rank_data2['value1']):
                return 2
            else:
                return 0
        elif rank_data1['rank'] == 8 or rank_data1['rank'] == 7:
            for a in range(1, 3):
                if ranks.index(rank_data1['value'+str(a)]) > ranks.index(rank_data2['value'+str(a)]):
                    return 1
                elif ranks.index(rank_data1['value'+str(a)]) < ranks.index(rank_data2['value'+str(a)]):
                    return 2
            return 0
        elif rank_data1['rank'] == 6 or rank_data1['rank'] == 1:
            for a in range(0, 5):
                if ranks.index(rank_data1['value'][4-a]) > ranks.index(rank_data2['value'][4-a]):
                    return 1
                elif ranks.index(rank_data1['value'][4-a]) < ranks.index(rank_data2['value'][4-a]):
                    return 2
            return 0
        elif rank_data1['rank'] == 4 or rank_data1['rank'] == 3:
            for a in range(1, 4):
                if ranks.index(rank_data1['value'+str(a)]) > ranks.index(rank_data2['value'+str(a)]):
                    return 1
                elif ranks.index(rank_data1['value'+str(a)]) < ranks.index(rank_data2['value'+str(a)]):
                    return 2
            return 0
        elif rank_data1['rank'] == 2:
            for a in range(1, 5):
                if ranks.index(rank_data1['value'+str(a)]) > ranks.index(rank_data2['value'+str(a)]):
                    return 1
                elif ranks.index(rank_data1['value'+str(a)]) < ranks.index(rank_data2['value'+str(a)]):
                    return 2
            return 0
    return 0


start_time = time.time()
flag = True
count = 0
fo = open('p054_poker.txt', 'r+')
data = fo.read()
l = data.split('\n')
for i in l:
    p1 = i.split(' ')[:5]
    p2 = i.split(' ')[5:]
    if who_win(p1, p2) == 1:
        # print(p1, p2)
        count += 1
    elif who_win(p1, p2) == 0:
        # print(p1, p2)
        pass
print('result is ', count)
print('total time is ', time.time() - start_time, 'ms')
