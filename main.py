from chessboard import ChessBoard

DUMMY_AGENT = "dummy"

MINIMAX_AGENT = "minimax"
DEPTH = 2

game = ChessBoard(MINIMAX_AGENT, DEPTH)
game.play()