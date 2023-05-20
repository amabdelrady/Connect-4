import tkinter as tk
from random import randint
from tkinter import messagebox

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
SQUARE_SIZE = 80
RADIUS = SQUARE_SIZE // 2 - 5
PLAYER1_COLOR = 'red'
PLAYER2_COLOR = 'yellow'
EMPTY_COLOR = 'white'
AI_DELAY = 500

# Create the game board
board = [['' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Set up the window
window = tk.Tk()
window.title('Connect Four')

# Set up the canvas
canvas = tk.Canvas(window, width=BOARD_WIDTH * SQUARE_SIZE, height=(BOARD_HEIGHT + 1) * SQUARE_SIZE)
canvas.pack()

# Create the difficulty selector
difficulty_var = tk.StringVar()
difficulty_var.set('Easy')
difficulty_label = tk.Label(window, text='Difficulty:', font=('Arial', 14))
difficulty_label.pack(side=tk.LEFT)
difficulty_menu = tk.OptionMenu(window, difficulty_var, 'Easy', 'Medium', 'Hard')
difficulty_menu.pack(side=tk.LEFT)

# Create the reset button
def reset():
    global board
    board = [['' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    canvas.delete('all')
    draw_board()
reset_button = tk.Button(window, text='Reset', font=('Arial', 14), command=reset)
reset_button.pack(side=tk.RIGHT)