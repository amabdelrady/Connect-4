# Computer move
def computer_move():
    if check_win('O'):
        return
    difficulty = difficulty_var.get()
    if difficulty == 'Easy':
        column = randint(0, BOARD_WIDTH - 1)
    elif difficulty == 'Medium':
        column = minimax(4, True, -float('inf'), float('inf'), 'O')[1]
    else:
        column = minimax(6, True, -float('inf'), float('inf'), 'O')[1]
    if make_move(column, 'O'):
        window.after(AI_DELAY, player_move)

# Minimax algorithm with alpha-beta pruning
def minimax(depth, maximizing_player, alpha, beta, player):
    if depth == 0 or check_win('X') or check_win('O'):
        if check_win('X'):
            return [-100000, None]
        elif check_win('O'):
            return [100000, None]
        else:
            return [0, None]
    if maximizing_player:
        max_score = -float('inf')
        best_column = None
        for column in range(BOARD_WIDTH):
            if is_valid_move(column):
                make_move(column, player)
                score = minimax(depth - 1, False, alpha, beta, 'X')[0]
                undo_move(column)
                if score > max_score:
                    max_score = score
                    best_column = column
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
        return [max_score, best_column]
    else:
        min_score = float('inf')
        best_column = None
        for column in range(BOARD_WIDTH):
            if is_valid_move(column):
                make_move(column, player)
                score = minimax(depth - 1, True, alpha, beta, 'O')[0]
                undo_move(column)
                if score < min_score:
                    min_score = score
                    best_column = column
                beta = min(beta, score)
                if alpha >= beta:
                    break
        return [min_score, best_column]