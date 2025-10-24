import argparse

from chessboard import ChessBoard

AGENTS = ["dummy", "minimax", "pruning"]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=AGENTS, default="dummy")
    parser.add_argument("--depth", type=int, default=2)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.agent == "dummy":
        args.depth = None

    game = ChessBoard(args.agent, args.depth)
    game.play()