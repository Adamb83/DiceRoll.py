

def tie_breaker():
    # importing the random module
    import random
    player1 = ""
    player2 = ""
    #print(random.randint(1,6))
    p1_score = int 
    p2_score = int
    win_score = int 
    #Animation Dice Function
    import time 
    import os
    global i
    i = 1

    # Player 1 Press enter to roll
    player1 = (input("Tie Breaker Round! Player 1 Press enter to roll"))
    print(open('dice1.txt', 'r').read()) 
    time.sleep(.3)
    os.system('cls')
    print(open('dice2.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice3.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice4.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice5.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice6.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice1.txt', 'r').read()) 
    time.sleep(.2)
    os.system('cls')
    print(open('dice2.txt', 'r').read())
    time.sleep(0.15) 
    os.system('cls')
    print(open('dice3.txt', 'r').read())
    time.sleep(0.1) 
    os.system('cls')
    if player1 == (""):
        i = 2
        p1_score = (random.randint(1,6))
        print ("Player 1 Rolls a " + str(int(p1_score)))                    # print player 1 number
    else:
        print ("Invalid Input") 

    # player 2 press enter to roll

    player2 = (input("Player 2 Press enter to roll"))
    print(open('dice1.txt', 'r').read()) 
    time.sleep(.3)
    os.system('cls')
    print(open('dice2.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice3.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice4.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice5.txt', 'r').read())
    time.sleep(0.3) 
    os.system('cls')
    print(open('dice6.txt', 'r').read())
    time.sleep(0.25 ) 
    os.system('cls')
    print(open('dice1.txt', 'r').read()) 
    time.sleep(.2)
    os.system('cls')
    print(open('dice2.txt', 'r').read())
    time.sleep(0.15) 
    os.system('cls')
    print(open('dice3.txt', 'r').read())
    time.sleep(0.1) 
    os.system('cls')
    if player2 == (""):
        i = 2
        p2_score = (random.randint(1,6))
        print ("Player 2 Rolls a " + str(int(p2_score)))                   # print player 2 number
    else:
        print ("Invalid Input") 


    # highest number wins round one, print "the winner is'
    if p2_score > p1_score:
        print ("Player 2 wins the tie breaker with a score of: " + str(int(p2_score)))
        win_score = p2_score
    if p2_score == p1_score:
        print ("Tie Breaker Death Match Continues, Press enter to begin")
        win_score = p1_score
    elif p1_score > p2_score:
        print ("Player 1 wins tie breaker round with a score of: " + str(int(p1_score))) 
        win_score = p1_score



    if win_score == 1:
        print(open('dice1.txt', 'r').read()) 
    if win_score == 2:
        print(open('dice2.txt', 'r').read()) 
    if win_score == 3:
        print(open('dice3.txt', 'r').read()) 
    if win_score == 4:
        print(open('dice4.txt', 'r').read()) 
    if win_score == 5:
        print(open('dice5.txt', 'r').read()) 
    if win_score == 6: 
        print(open('dice6.txt', 'r').read()) 

    ()



# importing the random module
import random
player1 = ""
player2 = ""
#print(random.randint(1,6))
p1_score = int 
p2_score = int
win_score = int 
#Animation Dice Function
import time 
import os
global i
i = 1

# Player 1 Press enter to roll
player1 = (input("Player 1 Press enter to roll"))
print(open('dice1.txt', 'r').read()) 
time.sleep(.3)
os.system('cls')
print(open('dice2.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice3.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice4.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice5.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice6.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice1.txt', 'r').read()) 
time.sleep(.2)
os.system('cls')
print(open('dice2.txt', 'r').read())
time.sleep(0.15) 
os.system('cls')
print(open('dice3.txt', 'r').read())
time.sleep(0.1) 
os.system('cls')
if player1 == (""):
    i = 2
    p1_score = (random.randint(1,6))
    print ("Player 1 Rolls a " + str(int(p1_score)))                    # print player 1 number
else:
    print ("Invalid Input") 

# player 2 press enter to roll

player2 = (input("Player 2 Press enter to roll"))
print(open('dice1.txt', 'r').read()) 
time.sleep(.3)
os.system('cls')
print(open('dice2.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice3.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice4.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice5.txt', 'r').read())
time.sleep(0.3) 
os.system('cls')
print(open('dice6.txt', 'r').read())
time.sleep(0.25 ) 
os.system('cls')
print(open('dice1.txt', 'r').read()) 
time.sleep(.2)
os.system('cls')
print(open('dice2.txt', 'r').read())
time.sleep(0.15) 
os.system('cls')
print(open('dice3.txt', 'r').read())
time.sleep(0.1) 
os.system('cls')
if player2 == (""):
    i = 2
    p2_score = (random.randint(1,6))
    print ("Player 2 Rolls a " + str(int(p2_score)))                   # print player 2 number
else:
    print ("Invalid Input") 


# highest number wins round one, print "the winner is'
if p2_score > p1_score:
    print ("Player 2 wins with a score of: " + str(int(p2_score)))
    win_score = p2_score
if p2_score == p1_score:
    print ("Round tied")
    win_score = p1_score
    tie_breaker () 
elif p1_score > p2_score:
    print ("Player 1 wins with a score of: " + str(int(p1_score))) 
    win_score = p1_score



if win_score == 1:
    print(open('dice1.txt', 'r').read()) 
if win_score == 2:
    print(open('dice2.txt', 'r').read()) 
if win_score == 3:
    print(open('dice3.txt', 'r').read()) 
if win_score == 4:
    print(open('dice4.txt', 'r').read()) 
if win_score == 5:
    print(open('dice5.txt', 'r').read()) 
if win_score == 6: 
    print(open('dice6.txt', 'r').read()) 


# play round two yes/no?
# print player number with the highest score Wins

