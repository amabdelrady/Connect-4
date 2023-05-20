



# Draw the board
def draw_board():
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):
            x1 = column * SQUARE_SIZE
            y1 = (row + 1) * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill=EMPTY_COLOR, outline='black', width=2)
            if board[row][column] == 'X':
                canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=PLAYER1_COLOR, outline='black', width=2)
            elif board[row][column] == 'O':
                canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=PLAYER2_COLOR, outline='black', width=2)

# Check for a win
def check_win(player):
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH - 3):
            if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column + 3] == player:
                return True
    for row in range(BOARD_HEIGHT - 3):
        for column in range(BOARD_WIDTH):
            if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column] == player:
                return True
    for row in range(BOARD_HEIGHT - 3):
        for column in range(BOARD_WIDTH - 3):
            if board[row][column] == board[row + 1][column + 1] == board[row + 2][column + 2] == board[row + 3][column + 3] == player:
                return True
    for row in range(3, BOARD_HEIGHT):
        for column in range(BOARD_WIDTH - 3):
            if board[row][column] == board[row - 1][column + 1] == board[row - 2][column + 2] == board[row - 3][column + 3] == player:
                return True
    return False