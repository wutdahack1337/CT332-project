import os
import pygame
import chess

CELL_SIZE = 90
BOARD_SIZE = CELL_SIZE * 8
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
HIGHLIGHT = (0, 255, 255)

class ChessBoard:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        self.board = chess.Board()

        self.selected_square = None
        self.legal_moves = []

        self.pieces = {}
        piece_files = {
            'P': 'wP.png', 'N': 'wN.png', 'B': 'wB.png', 'R': 'wR.png', 'Q': 'wQ.png', 'K': 'wK.png',
            'p': 'bP.png', 'n': 'bN.png', 'b': 'bB.png', 'r': 'bR.png', 'q': 'bQ.png', 'k': 'bK.png'
        }
        for symbol, filename in piece_files.items():
            path = os.path.join('img/pieces', filename)
            self.pieces[symbol] = pygame.image.load(path)

    def play(self):
        self.draw_board()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

        pygame.quit()

    def handle_click(self, pos):
        square = self.pos_to_square(pos)

        # Bỏ chọn
        if self.selected_square == square:
            self.selected_square = None
            self.legal_moves = []
            self.draw_board()
            return

        piece = self.board.piece_at(square)

        # Click vào piece và hiện legal moves
        if piece is not None and piece.color == self.board.turn:
            self.selected_square = square
            self.legal_moves = [move for move in self.board.legal_moves if move.from_square == square]
        elif self.selected_square is not None:
            move = chess.Move(self.selected_square, square)
            if move in self.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.legal_moves = []

        self.draw_board()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                self.draw_cell(row, col, WHITE if (row + col) % 2 == 0 else BLACK)

        for square in chess.SQUARES:
            self.draw_piece(square)

        if self.selected_square is not None:
            x, y = self.square_to_pos(self.selected_square)
            highlight_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
            highlight_surface.set_alpha(128)
            highlight_surface.fill(HIGHLIGHT)
            self.screen.blit(highlight_surface, (x, y))

        for move in self.legal_moves:
            x, y = self.square_to_pos(move.to_square)
            pygame.draw.circle(self.screen, HIGHLIGHT, (x + CELL_SIZE//2, y + CELL_SIZE//2), 19)

        pygame.display.flip()

    def draw_cell(self, row, col, color):
        x = col*CELL_SIZE
        y = row*CELL_SIZE
        pygame.draw.rect(self.screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    def draw_piece(self, square):
        piece = self.board.piece_at(square)
        if not piece:
            return
        
        img = self.pieces[piece.symbol()]
        x, y = self.square_to_pos(square)
        x += (CELL_SIZE - img.get_width())//2
        y += (CELL_SIZE - img.get_height())//2
        self.screen.blit(img, (x, y))

    def pos_to_square(self, pos):
        return chess.square(pos[0]//CELL_SIZE, 7-pos[1]//CELL_SIZE)

    def square_to_pos(self, square):
        return (square%8 * CELL_SIZE, (7 - square//8) * CELL_SIZE)

    
