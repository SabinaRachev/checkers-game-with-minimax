from copy import deepcopy
import pygame
from checkers.constants import WHITE, BLACK


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        # move is (row,col), skip is the pieces that we will skip
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            # draw_moves(game, board, piece)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def minimax(position, depth, max_player, game, alpha, beta):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game, alpha, beta)[0]
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, max_eval)
            if max_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game, alpha, beta)[0]
            min_eval = min(min_eval, evaluation)
            beta = min(beta, min_eval)
            if min_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break

        return min_eval, best_move


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()

