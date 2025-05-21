import random
import requests
from datetime import datetime

# introduction and welcome message
print('\nWelcome to the World of Pokémon! \n')
player1name = input('Before we start, please enter your name: ')

def start_game():
    # this function is asking about playing a game / player types yes or no and returns true if yes and false if otherwise
    while True:
        print(f'Hello, {player1name}!\n')
        print('There will be 6 rounds in total in the game.')
        print('After each round, the winner of each duel will be announced.')
        print('At the end of the game, the winner of all rounds will be announced.')
        print('You can always finish the game earlier, or play again after the game finishes.\n')
        ready = input(f'So, {player1name}, would you like to play a game? ')
        if ready.lower() == 'yes':
            print('Nice! Let\'s start then.')
            break
        elif ready.lower() == 'no':
            print('No worries! Come back later if you change your mind.')
            return False
        else:
            print('Invalid answer. Please enter yes/no: ')
    return True

def player_pokemon():
    # player is making a choice what pokemon wants to use by its ID, then fetches the details from API
    # player types ID number / return dictionary containing the chosen pokemon data
    while True:
        pokemon_id = input('What is the Pokémon number you want to choose? ')
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
            print(f'You\'ve selected {pokemon["name"]}. You can\'t see your opponent\'s Pokémon now.')
            print(f'{pokemon["name"]} has the following stats:')
            print(f'hp is {pokemon["stats"][0]["base_stat"]}')
            print(f'attack is {pokemon["stats"][1]["base_stat"]}')
            print(f'speed is {pokemon["stats"][2]["base_stat"]}')
            print(f'defense is {pokemon["stats"][3]["base_stat"]}')
            return pokemon
        else:
            print('Invalid Pokémon number. Please try again.')

def random_pokemon():
    # opponent gets random pokemon by generating a random number between 1 and 151
    pokemon_number = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
    response = requests.get(url)
    pokemon = response.json()
    print(f'Your opponent received {pokemon["name"]}')
    print(f'{pokemon["name"]} has the following stats:')
    print(f'hp is {pokemon["stats"][0]["base_stat"]}')
    print(f'attack is {pokemon["stats"][1]["base_stat"]}')
    print(f'speed is {pokemon["stats"][2]["base_stat"]}')
    print(f'defense is {pokemon["stats"][3]["base_stat"]}')
    return pokemon

def get_stat_value(pokemon, stat_choice):
    # this gets the value of specified stats / stat_choice indicates which stat to retrieve
    # returns base stat value of the chosen stat
    stat_map = {
        'hp': 0,
        'attack': 1,
        'defense': 3,
        'speed': 2
    }
    return pokemon['stats'][stat_map[stat_choice]]['base_stat']

def game():
    # game logic / player chooses a stat / opponent's pokemon / compares the stats to determine the winner
    my_pokemon = player_pokemon()
    while True:
        stat_choice = input("Which stat do you want to use? (hp / attack / speed / defense): ")
        if stat_choice in ['hp', 'attack', 'speed', 'defense']:
            break
        else:
            print("Invalid answer. Please, select from hp, attack, speed, or defense.")

    opponent_pokemon = random_pokemon()

    my_stat = get_stat_value(my_pokemon, stat_choice)
    opponent_stat = get_stat_value(opponent_pokemon, stat_choice)

    if my_stat > opponent_stat:
        print('Congrats! You\'re the winner of this round! :)')
        return 1 # player wins
    elif my_stat < opponent_stat:
        print('Sorry, you loose this round :(')
        return -1 # opponent wins
    else:
        print('It\'s a draw!')
        return 0 # draw

def play_again():
    # asks to play again
    # player types yes or no and returns true if yes and false if otherwise
    while True:
        ready = input('Fancy playing again? ')
        if ready.lower() == 'yes':
            print('Excellent!')
            return True
        elif ready.lower() == 'no':
            print('It was a great game! Come back later soon!.')
            return False
        else:
            print('Invalid answer. Please enter yes/no: ')

def write_score_to_file(player_score, opponent_score):
    # writes a score to a file, without overwriting it / adds date and time to keep track of when the game was played
    current_time = datetime.now().strftime('%Y-%m--%d %H:%M:%S')
    with open('pokemon_top_trumps_game_scores.txt', 'a+') as text_file:
        text_file.write(f'{current_time} - {player1name}: {player_score}, Opponent Score: {opponent_score}\n')

def main():
    # logic of the game, keeps track of the results and rounds
    if start_game():
        while True:
            player_score = 0
            opponent_score = 0

            for round_number in range(1, 7):
                print(f"Round {round_number}")
                result = game()
                if result == 1:
                    player_score += 1
                elif result == -1:
                    opponent_score += 1

            print(f"\nFinal Score:\nYou: {player_score}\nOpponent: {opponent_score}")
            if player_score > opponent_score:
                print("Congratulations! You won the game!")
            elif player_score < opponent_score:
                print("Sorry! You lost the game!")
            else:
                print("It's a draw!")

            # writes the score in a file
            write_score_to_file(player_score, opponent_score)

            if not play_again():
                break

if __name__ == "__main__":
    main()


