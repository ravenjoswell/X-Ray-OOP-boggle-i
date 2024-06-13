import string, random

class BoggleBoard:

  alpha = string.ascii_uppercase

  def __init__(self):
    self.board = []
    for i in range(4):
      self.board.append(["_","_","_","_"])
    # self.board = line
      
  def __repr__(self) -> str:
    line = ""
    for i in range(4):
      for j in range(4):
        line += self.board[i][j]
      line += "\n"
    return line

  def shake(self):
    # print(self.board)
    for i in range(4):
      # print(f"index i {i}")
      for j in range(4):
        newvar = random.choice(self.alpha) + "  "
        # print(f"\tindex j {newvar}")
        self.board[i][j] = newvar 
    # print(self.board)


newboard = BoggleBoard()
newboard.shake()
print(newboard, "\n")
newboard.shake()
print(newboard, "\n")
newboard.shake()
print(newboard, "\n")
newboard.shake()
print(newboard, "\n")