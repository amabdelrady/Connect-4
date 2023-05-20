# Make a move
def make_move(column, player):
    global board
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == '':
            board[row][column] = player
            draw_board()
            if check_win(player):
                canvas.unbind('<Button-1>')
                if player == 'X':
                    tk.messagebox.showinfo('Game Over', 'You win!')
                else:
                    tk.messagebox.showinfo('Game Over', 'The computer wins!')
            return True
    return False

# Player move
def player_move(event):
    if check_win('X'):
        return
    column = event.x // SQUARE_SIZE
    if make_move(column, 'X'):
        window.after(AI_DELAY, computer_move)