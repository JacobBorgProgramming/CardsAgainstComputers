import random

playedcards = ["1","2"]
random.shuffle(playedcards)

mycards = ["1","2","3","4","5","6","7"]

mycards2 = ["1","2","3","4","5","6"]

mycards3 = ["1","2","3","4","5"]

random.shuffle(mycards)
random.shuffle(mycards2)
random.shuffle(mycards3)

judge = random.choice(playedcards)

play = random.choice(mycards)
play2 = random.choice(mycards2)
play3 = random.choice(mycards3)

action = input('What am I doing... ')

if action == 'judging':
    print(" ")
    print("Card "+judge+" wins")

if action == 'playing':
    print(" ")
    print("I will play "+play)

if action == 'playing2':
    print(" ")
    print("I will play "+play)
    playing2 = input('Type in "next" when ready... ')
    if playing2 == 'next':
        print(" ")
        print("I will play "+play2)

if action == 'playing3':
    print(" ")
    print("I will play "+play)
    playing3 = input('Type in "next" when ready... ')
    if playing3 == 'next':
        print(" ")
        print("I will play "+play2)
        playing4 = input('Type in "next" when ready... ')
        if playing4 == 'next':
            print(" ")
            print("I will play "+play3)
