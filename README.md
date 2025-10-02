# 🎮 Math Duel – Subtraction Game with Minimax AI

This project implements a **turn-based subtraction game** where two players (Player 1 = MAX and Player 2 = MIN/AI) compete to reach zero.  
The AI opponent uses the **Minimax algorithm with Alpha-Beta pruning** to make optimal moves.

## ✨ Features
- Start with a configurable number (default: 16).
- Players can subtract **1, 2, or 3** (customizable).
- AI opponent (MIN) plays optimally using Minimax.
- Win condition: the player who makes the number exactly zero wins.
- Includes Alpha-Beta pruning for faster AI decisions.

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/math-duel-minimax.git
   cd math-duel-minimax
Run the game:
python math_duel.py

🛠️ Example Gameplay
*Current number: 16
*Player 1's turn (MAX)
*Allowed moves: [1, 2, 3]

👉 Player chooses 3
 *Current number: 13
 *AI's turn (MIN)
 *AI chooses 1

📂 File Structure
math-duel-minimax/
│── math_duel.py        # Main game logic (your code)
│── README.md           # Project documentation
│── requirements.txt    # Python dependencies

📦 Requirements
*Python 3.x
*No external libraries required (only math and time from Python standard library).

🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

📜 License
This project is licensed under the MIT License.
