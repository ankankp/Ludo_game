# 🎲 Ludo Game — Python + Pygame

A fully functional digital recreation of the classic **Ludo board game** built using **Python** and **Pygame**.
This project implements real Ludo gameplay mechanics with a clean modular architecture, making it ideal for learning game development and OOP design.

---

##  Features

*  Dice rolling system
*  4-player turn-based gameplay
* Multi-token movement
*  Safe tile protection
*  Capture / kill system
*  Finish lane mechanics
*  Exact roll to finish
*  Win detection
*  Modular code structure
*  Pygame rendering engine

---

##  Tech Stack

* **Language:** Python 3
* **Library:** Pygame
* **Paradigm:** Object-Oriented Programming
* **Graphics:** Custom drawn board / image board

---

##  Project Structure

```
ludo_game/
│
├── main.py              # Game loop & event handling
├── settings.py          # Screen & config settings
│
├── board/
│   ├── board.py         # Board rendering
│   └── path.py          # Movement paths & finish lanes
│
├── player/
│   └── player.py        # Player & token logic
│
├── dice/
│   └── dice.py          # Dice rolling system
│
└── assets/
    └── board.png        # Board image (optional UI)
```

---

##  How to Play

1. Press **SPACE** to roll the dice
2. Roll **6** to spawn a token
3. Tokens move along the board path
4. Landing on opponents captures them
5. Safe tiles protect tokens
6. Complete the loop to enter finish lane
7. First player to finish all tokens wins 

---

##  Game Mechanics Implemented

* Token spawning rules
* Turn rotation system
* Extra turn on rolling 6
* Safe zone immunity
* Finish lane entry gates
* Exact roll finish requirement
* Capture restrictions inside finish lanes

---

## Installation & Run

### Clone Repo

```bash
git clone https://github.com/your-username/ludo-game.git
cd ludo-game
```

### Install Dependencies

```bash
pip install pygame
```

###  Run Game

```bash
python main.py
```

---

## 📸 Screenshots

*Add gameplay screenshots here*

Example:

```
assets/screenshots/gameplay.png
```

---

##  Future Improvements

* Mouse token selection
* Dice roll animation
* Sound effects
* AI players
* Online multiplayer
* Mobile adaptation

---

## Contributing

Pull requests are welcome.
For major changes, please open an issue first.

---

##  License

This project is open-source and available under the **MIT License**.

---

##  Author

**Ankan Kumar Panja**
CSE Engineer • Game Dev Enthusiast • Python Developer

---

⭐ If you like this project, don’t forget to star the repo!
