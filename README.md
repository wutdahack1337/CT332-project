# CT332-project
Tham khảo: [simple-chess-ai](https://github.com/lhartikk/simple-chess-ai)

# How to run
```
pip install python-chess pygame
python main.py --help
python main.py --agent="minimax" --depth=2
```

# TODO
- [x] Move generation and board visualization
- [x] Dummy agent: Random move
- [x] Minimax agent:
    - [x] Add a-h, 1-8
    - [x] Add move sound
    - [x] Position evaluation
    - [x] Add optional depth (default depth is 2)
- [x] Alpha-beta pruning:
    - [x] Add cli
- [x] Improved evaluation function
- [ ] Log the AI status
