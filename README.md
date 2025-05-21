# top_trumps_pokemon
Top Trumps Pokemon Game in Python

Project made as a final assignment for the CFG Introduction to Python and the Apps course. 

It’s a battle simulation where the player chooses a Pokémon by its ID, and the opponent is assigned a random Pokémon. Opponent is a computer in this case. 
Players compare stats like HP, attack, speed, or defence over six rounds to determine a winner, with scores tracked and written to a file.

Challenges & Solutions:

1. API Integration
Challenge: learning how to fetch the Pokémon data from the PokeAPI
Solution: breaking down the API structure and using Python’s requests library to retrieve the JSON data effectively

2. Game Logic
Challenge: managing stat comparison logic, round tracking and deciding the winner
Solution: carefully structuring the code with proper functions for each game component

3. Code Scalability
Challenge: expanding the game to support multiple rounds and replay functionality
Solution: adding a main game loop and designing a play_again function to reset the game, while keeping the player interactions intuitive
