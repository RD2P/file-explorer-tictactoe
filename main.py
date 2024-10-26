# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #


# os is needed to create a new directory
import os

# image paths
black_path = 'black.png'
x_path = 'x.png'
o_path = 'o.png'

# Create canvas directory if it doesn't already exist
if not os.path.exists('canvas'):
  os.mkdir('canvas')

# Path of directory where we'll play the game
canvas_dir = './canvas/'

def paint_board():
  '''
  Create 9 blank images in the canvas directory to act as a tic tac toe grid, assuming:
  1. The user has opened file explorer and set the view to 'large icons'
  2. The user has resized the file explorer window such that the 9 images are displayed into a 3x3 grid
  '''
  img_file = open(black_path,'rb')
  data = img_file.read()
  for i in range(1,10):
    f = open(canvas_dir + f"{i}.png",'wb')
    f.write(data)
    f.close()

def write_to_board(play_path, target):
  '''
  Changes a blank png in the canvas directory to either an X or an O
  Inputs:
    play_path: path to the image for which the player wants to play, either x_path or o_path
    target: number between 1-9 inclusive, the target png to be changed
  Returns: None
  '''
    
  with open(play_path, 'rb') as image:
    data = image.read()
    with open(canvas_dir + f"{target}.png", 'wb') as img_target:
      img_target.write(data)

def check_winner(player):
  '''
  Check if there's a win on the board.
  The corresponding grid numbers that make up horizontal, vertical, and diagonal:
  1 2 3
  4 5 6
  7 8 9
  Inputs: player, either 'x' or 'o'
  Returns: True - there is a win, False - there is no win
  '''
  horizontal =  [[1,2,3], [4,5,6], [7,8,9]]
  vertical = [[1,4,7], [2,5,8], [3,6,9]]
  diagonal = [[1,5,9], [3,5,7]]

  # List all directions, we'll loop through all directions and check if theres a win in each
  directions = [horizontal, vertical, diagonal]

  # See if there's a horizontal win, a vertical win, and a diagonal win
  for d in directions:
    for r in d:
      hit_count = 0
      for c in r:
        if board[c] == player:
          hit_count += 1
      if hit_count == 3:
        return True # return True if there's a win

  return False # return False if no win

# Paint blank board in file explorer
paint_board()
print("Welcome to File Explorer Tic Tac Toe 😂")
print("During your turn, enter a number between 1-9 to designate your play.")

# Initialize board state with board numbers as keys and initially all zero values
# As plays are made, the values will be updated the player occupying this space
# E.g. if player x plays on spot 1, the board will be updated to { 1: 'x', .... }
board = {
  1: 0, 2: 0, 3: 0,
  4: 0, 5: 0, 6: 0,
  7: 0, 8: 0, 9: 0
}

# Play loop
while True:
  x_play = input("\nPlayer X, what's your play (1-9)? ").strip()
  write_to_board(x_path, x_play)
  board[int(x_play)] = 'x'
  if check_winner('x'):
    print("\n\n\n=== 🥳🥳🥳 Player X, you win! 🥳🥳🥳 ===\n\n\n")
    break

  o_play = input("\nPlayer O, what's your play (1-9)? ")
  write_to_board(o_path, o_play)
  board[int(o_play)] = 'o'
  if check_winner('o'):
    print("\n\n\n=== 🥳🥳🥳 Player O, you win! 🥳🥳🥳 ===\n\n\n")
    break