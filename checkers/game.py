import pygame
from .board import Board
from .constants import WHITE, SQUARE_SIZE, BLUE, BLACK, RED


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
        self.winner_game = None

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            if self.turn == WHITE and self.board.white_left == 1 and self.valid_moves == {}:
                self.winner_game = BLACK
                return False
            elif self.turn == BLACK and self.board.black_left == 1 and self.valid_moves == {}:
                self.winner_game = WHITE
                return False
            return True

        return False

    # move the piece
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 35, 5)

    def winner(self):
        if self.winner_game is None:
            return self.board.winner()
        else:
            return self.winner_game

    def get_board(self):
        return self.board

    # check if only kings left
    def check_end_eval(self):
        if self.board.white_left == self.board.white_kings and self.board.black_left == self.board.black_kings:
            self.board.end_eval = True

    def ai_move(self, board):
        self.board = board
        self.change_turn()
