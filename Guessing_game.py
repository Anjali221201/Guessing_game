from random import shuffle
#logic of this game
#Initial list
#Shuffle list
#user guess
#check guess

#shuffle function
def shuffle_list(my_listt):
    shuffle(my_listt)
    return(my_listt)

#Player'guess function
def player_guess():
    guess=""
    while guess not in ['0','1','2']:
        guess=input("Pick a Number:0,1,2\n")

    return guess

#check guess function
def check_guess(my_listt,guess):
    if my_listt[guess]=="O":
        print("Correct!!")
    else:
        print("Wrong Guess!")
        print(my_listt)


#Initial list
my_list = [" "," ","O"]
#Shuffle list
mixedup_list= shuffle_list(my_list)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)
