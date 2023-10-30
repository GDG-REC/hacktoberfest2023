#Code for playing Dobble game

#In this game, the player will be given two cards each with a specific set of symbols. 
#Both the cards have exactly one symbol in common.
#Now the player has to exactly spot the symbol that is common to win.   

#import the necessary libraries
import string
import random

#Intialising a list to store alphabets as we are going to use alphabets as the symbols on both the cards
symbols=list(string.ascii_letters)

#Initialising two cards, each with 5 symbols
card1=[0]*5
card2=[0]*5

#position1 and position2 are same symbol positions in card1 and card2 respectively
position1=random.randint(0,4)
position2=random.randint(0,4)

#samesymbol is the symbol that is going to be common on both the cards
samesymbol=random.choice(symbols)
#remove the samesymbol from the remaining symbols list in order to avoid it getting repeated
symbols.remove(samesymbol)

#If both random positions are same, fill the position on both cards with samesymbol
if (position1==position2):
    card1[position1]=samesymbol
    card2[position1]=samesymbol
    
#If positions are different, first fill the respective samesymbol position of both the cards and then alternate samesymbol position of the opposite card
#Also remove the assigned symbols from symbols list
else:
    card1[position1]=samesymbol
    card2[position2]=samesymbol
    
    card1[position2]=random.choice(symbols)
    symbols.remove(card1[position2])

    card2[position1]=random.choice(symbols)
    symbols.remove(card2[position1])
    

#Fill other positions of both the cards with the remaining symbols list 
i=0
while(i<5):
    if (i!=position1 and i!=position2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
 
#Print the cards to start the game
print(card1)
print(card2)

#Get the symbol spotted ny the player
ch=input("Spot the similar symbol: ")

#Compare it with the samesymbol that was generated and print results accordingly
if (ch==samesymbol):
    print("Yesss! You won!")
else:
    print("Oops! You lost!")
