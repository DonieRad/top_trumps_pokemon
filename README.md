Top Trumps Pokémon Game

A text-based Python game inspired by the classic Top Trumps card game, using live data from the PokéAPI. The player selects a Pokémon by its ID, while the opponent (the computer) is assigned a random Pokémon. The battle takes place over 6 rounds based on selected stats, with final scores saved to a local file.

---

Features:
+ Play 6 rounds of stat-based Pokémon battles
+ Choose your own Pokémon by ID
+ Random opponent Pokémon each round
+ Compare stats: HP, Attack, Speed, or Defense
+ Score tracking with round-by-round results
+ Results logged to a .txt file with date and time
+ Replay the game as many times as you'd like

---

How It Works:
1. Player inputs their name and is asked if they want to play.
2. Player chooses a Pokémon by its Pokédex ID (1–151 recommended).
3. A random opponent Pokémon is generated using the API.
4. The player selects a stat to compare.
5. The stat values are compared — the winner is determined for that round.
6. After 6 rounds, the final winner is announced.
7. Game results are logged to a local text file.
8. The player is prompted to play again.

---

Technologies Used
* Python 3
* requests – For fetching Pokémon data from the PokéAPI
* datetime – For recording scores with timestamps
* PokéAPI – Free RESTful Pokémon data API

---

Lessons Learned:
+ API Integration:
  Learned how to navigate and fetch data from RESTful APIs using requests.

+ Game Logic:
  Designed multiple game loops, stat comparisons, and scorekeeping.

+ Clean Code:
  Applied functions and user prompts to keep the experience interactive and modular.

+ Persistence:
  Used file handling to store game data persistently.


---



Project developed by DonieRad(Dorota Radecka) as part of the CFG Introduction to Python course.
