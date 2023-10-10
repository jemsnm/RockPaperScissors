import getpass

Rock = 0
Paper = 1
Scissors = 2

options = {
  "rock": Rock,
  "paper": Paper,
  "scissors": Scissors
}

def rock_paper_scissors():
    print('Welcome! Get ready to play rock, paper, scissors')
    message = ''
    player_1_score = 0
    player_2_score = 0
    game = True
    while game:
        player_1_choice = getpass.getpass('\nPlayer 1 enter your choice: ').lower()
        player_1_choice = get_choice(player_1_choice)

        player_2_choice = getpass.getpass('Player 2 make your choice: ').lower()
        player_2_choice = get_choice(player_2_choice)

        if player_1_choice == player_2_choice:
            message = f'\n Both players chose {get_option_key(player_1_choice)}, no one gets a point!'
        elif player_1_choice == Rock:
            if player_2_choice == Scissors:
                player_1_score += 1
                message = get_message(True, player_1_choice, player_2_choice)
            else:
                player_2_score += 1
                message = get_message(False, player_1_choice, player_2_choice)    
        elif player_1_choice == Scissors:
            if player_2_choice == Paper:
                player_1_score += 1
                message = get_message(True, player_1_choice, player_2_choice)
            else:
                player_2_score += 1
                message = get_message(False, player_1_choice, player_2_choice)
        elif player_1_choice == Paper:
            if player_2_choice == Rock:
                player_1_score += 1
                message = get_message(True, player_1_choice, player_2_choice)
            else:
                player_2_score += 1
                message = get_message(False, player_1_choice, player_2_choice)
        
        print(message)

        if player_1_score == 3:
            print('\nPlayer 1 wins!')
            get_score(player_1_score, player_2_score)
            game = play_again()
            if game:
                player_2_score = 0
                player_1_score = 0
        elif player_2_score == 3:
            print('\nPlayer 2 wins!')
            get_score(player_1_score, player_2_score)
            game = play_again()
            if game:
                player_2_score = 0
                player_1_score = 0
        else:
            get_score(player_1_score, player_2_score)
            continue
            
def get_choice(choice):
    if choice not in options:
        get_choice(getpass.getpass('You can only choose rock, paper or scissors! Please enter your choice: ').lower())
    else:
        return options[choice]

def get_message(player_1_win, player_1_choice, player_2_choice):
    player_1_choice_value = get_option_key(player_1_choice)
    player_2_choice_value = get_option_key(player_2_choice)
    if player_1_win:
        return f'\nPlayer 1 gets a point!\nPlayer 1 chose: {player_1_choice_value}\nPlayer 2 chose: {player_2_choice_value}'
    else:
        return f'\nPlayer 2 gets a point!\nPlayer 1 chose: {player_1_choice_value}\nPlayer 2 chose: {player_2_choice_value}'

def get_option_key(choice):
    for key, value in options.items():
        if choice == value:
            return key
    
def get_score(player_1_score, player_2_score):
    print(f'Player 1 Score: {player_1_score}')
    print(f'Player 2 Score: {player_2_score}')

def play_again():
    play_game = str(input('\nDo you want to play again?(y/n): ')).lower()
    if play_game not in ['y', 'n']:
        print('Please choose y or n: ')
        play_again()
    elif play_game == 'n':
        return False
    else:
        return True
    
rock_paper_scissors()