import random

class DummyAgent():
    def __init__(self, board):
        self.board = board

    def get_action(self):
        return random.choice(list(self.board.legal_moves))