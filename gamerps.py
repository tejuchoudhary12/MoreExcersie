from random import randint

def win(player_choice):
    print("You Win !")

def lose(player_choice):
    print("You Lose")

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print(player_choice,computer_choice,"=====")
    if player_choice == computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        win(player_choice)
    elif player_choice == 'paper' and computer_choice == 'scissors':
        lose(player_choice)
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win(player_choice)
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose(player_choice)
    elif player_choice == 'paper' and computer_choice == 'rock':
        win(player_choice)
    elif player_choice == 'rock'and computer_choice == 'paper':
        lose(player_choice)
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break
