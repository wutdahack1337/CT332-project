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

piece_values = {
    'p': 10, # pawn
    'b': 30, # bishop
    'n': 30, # knight
    'r': 50, # rook
    'q': 90, # queen
    'k': 900, # king
}

pawn_eval_white = [
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
]
pawn_eval_black = list(reversed(pawn_eval_white))

knight_eval = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]

bishop_eval_white = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]
bishop_eval_black = list(reversed(bishop_eval_white))

rook_eval_white = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]
rook_eval_black = list(reversed(rook_eval_white))

queen_eval = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

king_eval_white = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]
king_eval_black = list(reversed(king_eval_white))

class MinimaxAgent():
    def __init__(self, board, depth=2):
        self.board = board
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
            outcome = self.board.outcome()
            if outcome.winner == chess.BLACK:
                return 9999 # Black wins
            elif outcome.winner == chess.WHITE:
                return -9999 # White wins
            else:
                return 0 # Draw
        
        eval = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                value = piece_values[piece.symbol().lower()]
                if piece.color == chess.BLACK:
                    eval += value + get_pos_value(piece, square)
                else:
                    eval -= value + get_pos_value(piece, square)
        return eval
    
class PruningAgent():
    """
        Same with MinimaxAgent, but has alpha-beta pruning
    """
    def __init__(self, board, depth=2):
        self.board = board
        self.depth = depth

    def get_action(self):
        return self.minimax(self.depth, "black", -math.inf, math.inf)[0]

    def minimax(self, depth, player, alpha, beta):
        """
            return best_move, best_eval
        """
        if depth == 0:
            return None, self.evaluate_board()

        best_move = None
        if player == "black": # want to maximum agent score
            for move in self.board.legal_moves:
                self.board.push(move)
                _, eval = self.minimax(depth-1, "white", alpha, beta)
                self.board.pop()
                
                if eval > alpha:
                    best_move = move
                    alpha = eval

                if beta <= alpha: # alpha cutoff
                    break

            return best_move, alpha
        else: # want to minimum agent score
            for move in self.board.legal_moves:
                self.board.push(move)
                _, eval = self.minimax(depth-1, "black", alpha, beta)
                self.board.pop()
                
                if eval < beta:
                    best_move = move
                    beta = eval

                if beta <= alpha: # beta cutoff
                    break

            return best_move, beta

    def evaluate_board(self):
        if self.board.is_game_over():
            outcome = self.board.outcome()
            if outcome.winner == chess.BLACK:
                return 9999 # Black wins
            elif outcome.winner == chess.WHITE:
                return -9999 # White wins
            else:
                return 0 # Draw
        
        eval = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                value = piece_values[piece.symbol().lower()]
                if piece.color == chess.BLACK:
                    eval += value + get_pos_value(piece, square)
                else:
                    eval -= value + get_pos_value(piece, square)
        return eval
    
def get_pos_value(piece, square):
    symbol = piece.symbol().lower()
    row = square // 8
    col = square % 8
    if piece.color == chess.WHITE:
        if symbol == 'p':
            return pawn_eval_white[row][col]
        elif symbol == 'n':
            return knight_eval[row][col]
        elif symbol == 'b':
            return bishop_eval_white[row][col]
        elif symbol == 'r':
            return rook_eval_white[row][col]
        elif symbol == 'q':
            return queen_eval[row][col]
        elif symbol == 'k':
            return king_eval_white[row][col]
    else:
        if symbol == 'p':
            return pawn_eval_black[row][col]
        elif symbol == 'n':
            return knight_eval[row][col]
        elif symbol == 'b':
            return bishop_eval_black[row][col]
        elif symbol == 'r':
            return rook_eval_black[row][col]
        elif symbol == 'q':
            return queen_eval[row][col]
        elif symbol == 'k':
            return king_eval_black[row][col]
        
    return 0