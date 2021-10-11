import random
import sys
from tkinter import Tk
from tkinter import Canvas
from tkinter.constants import CENTER
from PIL import ImageTk, Image


def main():   
    
        #Initializes board to play game. 
            bck = Tk()
            bck.configure(background="green")
            bck.title("Speed")
            canvas = Canvas(bck, width = 600, height = 600)
      
        #initializes all pictures in file to be sized appropriately and set to a value
            # all the pictures for playing cards 
            back_image = ImageTk.PhotoImage(Image.open("card_back.png").resize((60,90), Image.ANTIALIAS))
            card1 = ImageTk.PhotoImage(Image.open("1s.gif").resize((60,90), Image.ANTIALIAS))
            card2 = ImageTk.PhotoImage(Image.open("2s.gif").resize((60,90), Image.ANTIALIAS))
            card3 = ImageTk.PhotoImage(Image.open("3s.gif").resize((60,90), Image.ANTIALIAS))
            card4 = ImageTk.PhotoImage(Image.open("4s.gif").resize((60,90), Image.ANTIALIAS))
            card5 = ImageTk.PhotoImage(Image.open("5s.gif").resize((60,90), Image.ANTIALIAS))
            card6 = ImageTk.PhotoImage(Image.open("6s.gif").resize((60,90), Image.ANTIALIAS))
            card7 = ImageTk.PhotoImage(Image.open("7s.gif").resize((60,90), Image.ANTIALIAS))
            card8 = ImageTk.PhotoImage(Image.open("8s.gif").resize((60,90), Image.ANTIALIAS))
            card9 = ImageTk.PhotoImage(Image.open("9s.gif").resize((60,90), Image.ANTIALIAS))
            card10 = ImageTk.PhotoImage(Image.open("10s.gif").resize((60,90), Image.ANTIALIAS))
            jack = ImageTk.PhotoImage(Image.open("11s.gif").resize((60,90), Image.ANTIALIAS))
            queen = ImageTk.PhotoImage(Image.open("12s.gif").resize((60,90), Image.ANTIALIAS))
            king = ImageTk.PhotoImage(Image.open("13s.gif").resize((60,90), Image.ANTIALIAS))
            blank = ImageTk.PhotoImage(Image.open("blank.gif").resize((60,90), Image.ANTIALIAS))
            # "Congradulations for winning picture" for player 1 and player 2
            p1win = ImageTk.PhotoImage(Image.open("p1wins.png").resize((300,300), Image.ANTIALIAS))
            p2win = ImageTk.PhotoImage(Image.open("p2wins.png").resize((300,300), Image.ANTIALIAS))

            # pictures that show the number of cards in the deck that is remaining
            no0 = ImageTk.PhotoImage(Image.open("0.gif").resize((40,60), Image.ANTIALIAS))
            no1 = ImageTk.PhotoImage(Image.open("1.gif").resize((40,60), Image.ANTIALIAS))
            no2 = ImageTk.PhotoImage(Image.open("2.gif").resize((40,60), Image.ANTIALIAS))
            no3 = ImageTk.PhotoImage(Image.open("3.gif").resize((40,60), Image.ANTIALIAS))
            no4 = ImageTk.PhotoImage(Image.open("4.gif").resize((40,60), Image.ANTIALIAS))
            no5 = ImageTk.PhotoImage(Image.open("5.gif").resize((40,60), Image.ANTIALIAS))
            no6 = ImageTk.PhotoImage(Image.open("6.gif").resize((40,60), Image.ANTIALIAS))
            no7 = ImageTk.PhotoImage(Image.open("7.gif").resize((40,60), Image.ANTIALIAS))
            no8 = ImageTk.PhotoImage(Image.open("8.gif").resize((40,60), Image.ANTIALIAS))
            no9 = ImageTk.PhotoImage(Image.open("9.gif").resize((40,60), Image.ANTIALIAS))
            no10 = ImageTk.PhotoImage(Image.open("10.gif").resize((40,60), Image.ANTIALIAS))

             #global list of deck of cards. (the interates are all photoimages)
            deck = [card1, card1,card1,card1,card2,card2,card2,card2,card3,card3,card3,card3,card4,card4,card4,
            card4,card5,card5,card5,card5,card6,card6,card6,card6,card7,card7,card7,card7,card8,card8,card8,
            card8,card9,card9,card9,card9,card10,card10,card10,card10,jack,jack,jack,jack, queen, queen, queen,
            queen, king, king, king, king]

            # dictionary that connects each photo image to an integer. This is used to to see if the values 
            #are +1 or -1 of a card in middle deck. used in function valid_test()
            reference = {blank: None, card1: 1, card2: 2, card3: 3, card4: 4, card5: 5, card6: 6, card7: 7,
            card8: 8, card9: 9, card10: 10, jack: 11, queen: 12, king: 13}

            # a dictionary used to connect the picture that show deck number cards to coordinate accordingly
            #with how many cards are left in the deck.
            deck_number = {0: no0, 1: no0, 2: no0, 3: no0, 4: no0, 5: no0, 6: no1, 7: no2, 8: no3, 9: no4, 10: no5, 11: no6, 12: no7, 13: no8, 14: no9,
            15: no10}
        

             
            # initializes a player class that holds objects of hand,middle,pile lists. 
            # these separate lists are referred to to mutate lists with functions from player input
            
            class player():
                # automatically makes a random hand pile, middle pile, and pick up pile when class 
                # is called. 
                def __init__ (self, hand, middle, pile):
                    self.hand = hand
                    self.hand = self.make_hand(self.hand)
                    self.pile = pile
                    for _ in range(0,5):
                        self.pile.append(blank)
                    self.pile = self.make_pile(self.pile) 
                    self.middle = middle
                    self.middle = self.make_middle(self.middle)
            
                def make_hand(self, hand_list):  # makes the players hands 
                    random.shuffle(deck)
                    for i in range(0,5): 
                        card = deck[i]
                        deck.pop(i)
                        hand_list.append(card)
                    return hand_list
                        

                def make_pile(self, pile_list):  # makes each player's pile from which they can pick up cards from and place into their hands
                    random.shuffle(deck)
                    for i in range(0,10):
                        card = deck[i]
                        deck.pop(i)
                        pile_list.append(card)
                    return pile_list

                def make_middle(self, middle_list):  # makes the middle pile where the player flips from to add cards +1 or -1 from hand deck
                    random.shuffle(deck)
                    for i in range(0, 7):
                        card = deck[i]
                        deck.pop(i)
                        middle_list.append(card)
                    return middle_list

            # automatically initizliaed Player 1 and Player 2 class when main() is called. 
            Player1 = player([],[],[]) # initialize
            Player2 = player([],[],[])

            #positioning the cards
            ## player1 pick up pile 
            canvas.create_image(70, 70, anchor=CENTER, image=back_image)
                ## player1, hand cards
            canvas.create_image(180, 130, anchor=CENTER, image=Player1.hand[0])
            canvas.create_image(240, 130, anchor=CENTER, image=Player1.hand[1])
            canvas.create_image(300, 130, anchor=CENTER, image=Player1.hand[2])
            canvas.create_image(360, 130, anchor=CENTER, image=Player1.hand[3])
            canvas.create_image(420, 130, anchor=CENTER, image=Player1.hand[4])
                ## player 1 middle back_card (left)
            canvas.create_image(130, 300, anchor=CENTER, image=back_image)
                ## player 2 middle back_card (right)
            canvas.create_image(470, 300, anchor=CENTER, image=back_image)
                ## player 1 middle pile
            canvas.create_image(245, 300, anchor=CENTER, image=Player1.middle[len(Player1.middle)-1])
                ## player 2 midle pile 
            canvas.create_image(355, 300, anchor=CENTER, image=Player2.middle[len(Player2.middle)-1])
                ## player2 pick up pile 
            canvas.create_image(530, 530, anchor=CENTER, image=back_image)
                ## player2 hand cards
            canvas.create_image(180, 470, anchor=CENTER, image=Player2.hand[0])
            canvas.create_image(240, 470, anchor=CENTER, image=Player2.hand[1])
            canvas.create_image(300, 470, anchor=CENTER, image=Player2.hand[2])
            canvas.create_image(360, 470, anchor=CENTER, image=Player2.hand[3])
            canvas.create_image(420, 470, anchor=CENTER, image=Player2.hand[4])
                ## player1 deck number (number of cards remaining in pick up pile)
            canvas.create_image(70, 190, anchor=CENTER, image=deck_number[len(Player1.pile)])
                ## player2 deck number (number of cards remaining in pick up pile)
            canvas.create_image(530, 400, anchor=CENTER, image=deck_number[len(Player2.pile)])

            # custom function to add the indexed card from player's hand deck to the middle_deck
            def add_to_middle(player, middle_deck, index): 
                middle_deck.middle.append(player.hand[index])
                player.hand.pop(index)
                player.hand.append(player.pile[len(player.pile)-1])
                player.pile.pop(len(player.pile)-1)
                if middle_deck == Player1: 
                    canvas.create_image(245, 300, anchor=CENTER, image=middle_deck.middle[len(middle_deck.middle)-1])
                elif middle_deck == Player2: 
                    canvas.create_image(355, 300, anchor=CENTER, image=middle_deck.middle[len(middle_deck.middle)-1])
                if player == Player1:
                    canvas.create_image(180, 130, anchor=CENTER, image=player.hand[0])
                    canvas.create_image(240, 130, anchor=CENTER, image=player.hand[1])
                    canvas.create_image(300, 130, anchor=CENTER, image=player.hand[2])
                    canvas.create_image(360, 130, anchor=CENTER, image=player.hand[3])
                    canvas.create_image(420, 130, anchor=CENTER, image=player.hand[4])
                    canvas.create_image(70, 190, anchor=CENTER, image=deck_number[len(player.pile)])
                elif player == Player2:
                    canvas.create_image(180, 470, anchor=CENTER, image=player.hand[0])
                    canvas.create_image(240, 470, anchor=CENTER, image=player.hand[1])
                    canvas.create_image(300, 470, anchor=CENTER, image=player.hand[2])
                    canvas.create_image(360, 470, anchor=CENTER, image=player.hand[3])
                    canvas.create_image(420, 470, anchor=CENTER, image=player.hand[4])
                    canvas.create_image(530, 400, anchor=CENTER, image=deck_number[len(player.pile)])
            
            # returns true is the index of player's hand that is called is an appropriate card (+1 or -1)
            #to add to the middle pile 
            def valid_test(player, middle_deck, index):
                if reference[player.hand[index]] == (reference[middle_deck.middle[len(middle_deck.middle)-1]] + 1) or reference[player.hand[index]] == (reference[middle_deck.middle[len(middle_deck.middle)-1]] - 1) or reference[player.hand[index]] == 13 and reference[middle_deck.middle[len(middle_deck.middle)-1]] == 1 or reference[player.hand[index]] == 1 and reference[middle_deck.middle[len(middle_deck.middle)-1]] == 13:
                    return True
                
        
            # check to see if parameter player has run out of cards 
            def win_check(player):
                if player_check(player) == True:
                    if player == Player1:
                        canvas.create_image(300, 300, anchor=CENTER, image=p1win)
                    if player == Player2:
                        canvas.create_image(300, 300, anchor=CENTER, image=p2win)

                        
            # checks to see if there are any cards left in the hand_pile for both players 
            def player_check(player): 
                if player.hand[0] == blank:
                    return True

            
            def esc(event):
                sys.exit()

            # PLAYER 1 INPUT 
                #player presses 'a' to add index of 0 in hand pile to the middle pile
            def a(event):
                
                if valid_test(Player1, Player1, 0) == True:
                    add_to_middle(Player1, Player1, 0)
                    win_check(Player1)
         
                elif valid_test(Player1, Player2, 0) == True:
                    add_to_middle(Player1, Player2, 0)
                    win_check(Player1)

                #player presses 's' to add index of 1 in hand pile to the middle pile
            def s(event):
                
                if valid_test(Player1, Player1, 1) == True:
                    add_to_middle(Player1, Player1, 1)
                    win_check(Player1)
         
                elif valid_test(Player1, Player2, 1) == True:
                    add_to_middle(Player1, Player2, 1)
                    win_check(Player1)

                #player presses 'd' to add index of 2 in hand pile to the middle pile
            def d(event):
                
                if valid_test(Player1, Player1, 2) == True:
                    add_to_middle(Player1, Player1, 2)
                    win_check(Player1)
         
                elif valid_test(Player1, Player2, 2) == True:
                    add_to_middle(Player1, Player2, 2)
                    win_check(Player1)

                #player presses 'f' to add index of 3 in hand pile to the middle pile
            def f(event):
                
                if valid_test(Player1, Player1, 3) == True:
                    add_to_middle(Player1, Player1, 3)
                    win_check(Player1)
         
                elif valid_test(Player1, Player2, 3) == True:
                    add_to_middle(Player1, Player2, 3)
                    win_check(Player1)

                #player presses 'g' to add index of 4 in hand pile to the middle pile
            def g(event):
                
                if valid_test(Player1, Player1, 4) == True:
                    add_to_middle(Player1, Player1, 4)
                    win_check(Player1)
         
                elif valid_test(Player1, Player2, 4) == True:
                    add_to_middle(Player1, Player2, 4)
                    win_check(Player1)
            
            #PLAYER 2 INPUT
            
                #player presses 'h' to add index of 0 in hand pile to the middle pile
            def h(event):
                
                if valid_test(Player2, Player1, 0) == True:
                    add_to_middle(Player2, Player1, 0)
                    win_check(Player2)
         
                elif valid_test(Player2, Player2, 0) == True:
                    add_to_middle(Player2, Player2, 0)
                    win_check(Player2)

                #player presses 'j' to add index of 1 in hand pile to the middle pile
            def j(event):
                
                if valid_test(Player2, Player1, 1) == True:
                    add_to_middle(Player2, Player1, 1)
                    win_check(Player2)
         
                elif valid_test(Player2, Player2, 1) == True:
                    add_to_middle(Player2, Player2, 1)
                    win_check(Player2)

                #player presses 'k' to add index of 2 in hand pile to the middle pile
            def k(event):
                
                if valid_test(Player2, Player1, 2) == True:
                    add_to_middle(Player2, Player1, 2)
                    win_check(Player2)
         
                elif valid_test(Player2, Player2, 2) == True:
                    add_to_middle(Player2, Player2, 2)
                    win_check(Player2)

                #player presses 'l' to add index of 3 in hand pile to the middle pile
            def l(event):
                
                if valid_test(Player2, Player1, 3) == True:
                    add_to_middle(Player2, Player1, 3)
                    win_check(Player2)
         
                elif valid_test(Player2, Player2, 3) == True:
                    add_to_middle(Player2, Player2, 3)
                    win_check(Player2)

                #player presses ';' to add index of 4 in hand pile to the middle pile
            def colon(event):
                
                if valid_test(Player2, Player1, 4) == True:
                    add_to_middle(Player2, Player1, 4)
                    win_check(Player2)
         
                elif valid_test(Player2, Player2, 4) == True:
                    add_to_middle(Player2, Player2, 4)
                    win_check(Player2)

                
            #when both player agree there are no moves left, they press the 'up' key to 
            #change the card of the middle pile 
            def up(event):
                player1card = Player1.middle[0]
                player2card = Player2.middle[0]
                Player1.middle.pop(0)
                Player2.middle.pop(0)
                Player1.middle.append(player1card)
                Player2.middle.append(player2card)
                random.shuffle(Player1.middle)
                random.shuffle(Player2.middle)
                canvas.create_image(355, 300, anchor=CENTER, image=Player2.middle[len(Player2.middle)-1])
                canvas.create_image(245, 300, anchor=CENTER, image=Player1.middle[len(Player1.middle)-1])
            
            
            # function to bind a keyboard key to a method above
            
            bck.bind("<a>", a)
            bck.bind("<s>", s)
            bck.bind("<d>", d)
            bck.bind("<f>", f)
            bck.bind("<g>", g)
            
            bck.bind("<h>", h)
            bck.bind("<j>", j)
            bck.bind("<k>", k)
            bck.bind("<l>", l)
            bck.bind("<;>", colon)

            bck.bind("<Escape>", esc)
            
            bck.bind("<Up>", up)
      
            canvas.pack()
            bck.mainloop()
main()  
