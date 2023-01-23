#Main.py for Python Minesweeper Project
print("Welcome to MinesweePyr!")
diff_list = ["e", "m", "h", "easy", "medium", "hard"]
gameOver = False

class Game:
  def __init__(self, difficulty):
    if difficulty == "h" or difficulty == "hard":
      self.rows, self.columns = 20
    elif difficulty == "m" or difficulty == "medium":
      self.rows, self.columns = 10
    else:
      self.rows, self.columns = 5

print("Choose your difficulty:")
difficulty = input("Easy (E), Medium (M), or Hard (H)\n")
  if difficulty.lower() not in diff_list:
    print("Invalid entry. Game Over before it started.")
    gameOver = True
  else:
    sweep = Game(difficulty)

#GameLoop will go here
