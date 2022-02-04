#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_4_Plottinsg
import random


def simulate_gachapon(n_prizes):
    """
    Args:
        n_prizes: Number of possible prizes to win from a set
    Returns: How many tries it takes to win all the prizes
    """
    # Initialize a dictionary with a prize count of zero
    prizes = list(range(0, n_prizes))
    # print('prizes ', prizes)
    prize_dist = {}
    for prize in prizes:
        prize_dist[prize] = 0
    # Empty list to keep a running tally of prizes
    prize_list = []

    # Keep looping while there are any prizes with a count of 0
    while min(prize_dist.values()) < 1:
        # Draw a random number from possible prize range
        draw = random.randrange(0, n_prizes, 1)
        # Add new prize to current prizes
        prize_list.append(draw)
        # Add new prize to count of that same prize
        for key in prizes:
            if draw == key:
                prize_dist[key] += 1  # https://www.kite.com/python/answers/how-to-increment-a-value-in-a-dictionary-in-python
            # print('prize_dist ', prize_dist)
    else:
        return len(prize_list)


# if __name__ == "__main__":
#     simulate_gachapon(15)


"""
References: 
https://docs.python.org/3/library/random.html
https://www.delftstack.com/howto/python/python-list-from-1-to-n/
https://www.geeksforgeeks.org/python-initialize-a-dictionary-with-only-keys-from-a-list/
"""
