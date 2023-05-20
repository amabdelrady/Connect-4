# Check if a move is valid
def is_valid_move(column):
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == '':
            return True
    return False

# Undo a move
def undo_move(column):
    global board
    for row in range(BOARD_HEIGHT):
        if board[row][column] != '':
            board[row][column] = ''
            return

# Bind the canvas to mouse clicks
canvas.bind('<Button-1>', player_move)

# Draw the initial board
draw_board()

# Start the game
window.mainloop()