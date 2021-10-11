is_bored = True
cant_stop_wont_stop = False
has_homework = False

def play_2048(requirement1, requirement2, requirement3):
	return ((requirement1 and requirement2) and (not requirement3)) or (not (requirement2 and requirement3)) 

play_2048(is_bored, cant_stop_wont_stop, has_homework)

dictionary = {"vegies": ["carrot", "cilantro", "tomato"], "meat": ["sausage", "poke", "tuna"]}
make_list = ["poke", "ahi"]
def bake():
    print("baking your {0} pizza!".format(", ".join(make_list)))

def many():
    ## range(0,5)
    for i in range(0,5):
        print(i)

lst = [ "a", "p", "p", "l", "e"]

def list_up(lst):


    if len(lst) == 0:
        return []
    elif lst[0] in ["p", "e"]:
        return lst[0], lst[0], list_up(lst[1:])
    else: 
        return lst[0], list_up(lst[1:])

def count_sevens(num):
    count = 0 
    while num != 0: 
        if num % 10 == 7: 
            count += 1
        num = num // 10
    return count 

def printletter(word):
    for letter in word: 
        print(letter)

def anagram(word1,word2):
    occurrences = {}
    for word1_letter in word1:
        if word1_letter in occurrences:
            occurrences[word1_letter] += 1
        else:
            occurrences[word1_letter] = 1
    for word2_letter in word2:
        if word2_letter not in occurrences:
            return False
        else:
            occurrences[word2_letter] -= 1
    for letter, number in occurrences.items():
        if occurrences[letter] != 0:
            return False
    return True   