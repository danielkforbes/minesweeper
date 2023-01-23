#Main.py for Python Minesweeper Project
print("Welcome to MinesweePyr!")

class Game:
  pass

diff_list = ["e", "m", "h", "easy", "medium", "hard"]
print("Choose your difficulty:")
difficulty = input("Easy (E), Medium (M), or Hard (H)\n")
  if difficulty.lower() not in diff_list:
    print("Invalid entry. Game Over before it started.")
  else:
    sweep = Game(difficulty)
