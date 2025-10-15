import pygame
import chess

class ChessBoard:
    def __init__(self):
        # pygame.init()
        pygame.display.set_mode((666, 666))

        self.board = chess.Board()

    def handle_click(self, pos):
        print(pos)
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
        pygame.quit()




game = ChessBoard()
game.run()