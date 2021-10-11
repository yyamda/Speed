import random

deck = ["strings", "pokemon", "vaporeon", "flareon", "jolteon", "fairyeon", "pikachu", "pichu", 
        "raichu", "glaceon", "umbreon", "bagon", "salamander", "chimchar", "rayquaza", "metapod"]



# THIS IS TEST NUMBER 1
# Input: input should be a any list 
# Output: the list that was inputted with 5 iterates added at the end from the DECK global list

test_list1 = ["card5", "card1", "card9", "king", "queen"]

# THIS IS TEST NUMBER 2 
# Input: input should be any list 
# Output: the list that was inputted with 5 iterates added at the end from the DECK global list

test_list2 = ["squirtle", "torterra", "victini", "ochawatt", "piplup"]

# we used test_list2 and test_list1 as inputs for the make_hand

def make_hand(hand_list):  # makes the players hands 
                    random.shuffle(deck)
                    for i in range(0,5): 
                        card = deck[i]
                        deck.pop(i)
                        hand_list.append(card)
                    return hand_list
                        