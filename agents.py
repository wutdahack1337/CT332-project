import random
import math

import chess

class DummyAgent():
    """
        Random move
    """
    def __init__(self, board):
        self.board = board

    def get_action(self):
        return random.choice(list(self.board.legal_moves))

class MinimaxAgent():
    def __init__(self, board, depth=2):
        self.board = board
        
        self.piece_values = {
            'p': 10, # pawn
            'b': 30, # bishop
            'n': 30, # knight
            'r': 50, # rook
            'q': 90, # queen
            'k': 900, # king
        }

        self.depth = depth

    def get_action(self):
        return self.minimax(self.depth, "black")[0]

    def minimax(self, depth, player):
        """
            return best_move, best_eval
        """
        if depth == 0:
            return None, self.evaluate_board()

        best_move = None
        if player == "black": # want to maximum agent score
            best_eval = -math.inf
            for move in self.board.legal_moves:
                self.board.push(move)
                _, eval = self.minimax(depth-1, "white")
                self.board.pop()
                
                if eval > best_eval:
                    best_move = move
                    best_eval = eval
        else: # want to minimum agent score
            best_eval = math.inf
            for move in self.board.legal_moves:
                self.board.push(move)
                _, eval = self.minimax(depth-1, "black")
                self.board.pop()
                
                if eval < best_eval:
                    best_move = move
                    best_eval = eval

        return best_move, best_eval

    def evaluate_board(self):
        if self.board.is_game_over():
            if self.board.is_checkmate():
                if self.board.turn == chess.WHITE:
                    return 9999  # Black wins
                else:
                    return -9999   # White wins
            else:
                return 0  # Draw
        
        eval = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                value = self.piece_values[piece.symbol().lower()]
                if piece.color == chess.BLACK:
                    eval += value
                else:
                    eval -= value
        return eval