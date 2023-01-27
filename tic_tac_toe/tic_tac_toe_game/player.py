from tic_tac_toe_game.board_symbol import Move


class Player:
    __row: int
    __column: int

    def __init__(self, name: str, count: int):
        self.__name = name
        self.__symbol: Move
        if count == 1:
            self.__symbol = Move.O
        else:
            self.__symbol = Move.X

    def get_name(self) -> str:
        return self.__name

    def get_symbol(self) -> str:
        return self.__symbol.name

    def set_position(self, row: int, column: int):
        self.__row = row
        self.__column = column

    def get_row(self) -> int:
        return self.__row

    def get_column(self) -> int:
        return self.__column
