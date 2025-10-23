import argparse

from chessboard import ChessBoard

DUMMY_AGENT = "dummy"
MINIMAX_AGENT = "minimax"
PRUNING_AGENT = "pruning"
DEPTH = 2

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=[DUMMY_AGENT, MINIMAX_AGENT, PRUNING_AGENT], default=DUMMY_AGENT)
    parser.add_argument("--depth", type=int, default=2)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.agent == DUMMY_AGENT:
        args.depth = None

    game = ChessBoard(args.agent, args.depth)
    game.play()