from enum import Enum


class Move(Enum):
    O = "O"
    X = "X"
    EMPTY = " "

    def __init__(self, symbol: str):
        self.symbol = symbol
