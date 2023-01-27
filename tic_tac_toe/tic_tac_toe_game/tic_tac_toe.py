from typing import List

from tic_tac_toe_game.player import Player


class TicTacToe:

    def __init__(self):
        self.__board: List[List[str]] = [[" ", " ", " "],
                                         [" ", " ", " "],
                                         [" ", " ", " "]]
        self.__players: list[Player] = []
        self.__current_player: int = 0

    def register_player(self, player_name, player_number):
        self.__players.append(Player(player_name, player_number))

    def take_position(self, position):
        self.__validate_move_number(position)
        self.__set_player_position(position)
        self.__validate_available_position(position)
        self.__set_board()
        self.__adjust_current_player()

    def __set_player_position(self, position):
        position -= 1
        row: int = position // 3
        column: int = position % 3
        self.__players.__getitem__(self.__current_player).set_position(row, column)

    def get_board(self) -> []:
        return self.__board

    def get_players(self) -> list[Player]:
        return self.__players

    def __set_board(self) -> None:
        row: int = self.__players.__getitem__(self.__current_player).get_row()
        column: int = self.__players.__getitem__(self.__current_player).get_column()
        self.__board.__getitem__(row)[column] = self.__players.__getitem__(self.__current_player).get_symbol()

    def __adjust_current_player(self) -> None:
        self.__current_player += 1
        if self.__current_player > 1:
            self.__current_player = 0

    @staticmethod
    def __validate_move_number(move_number):
        if len(str(move_number)) > 1 or move_number < 1 or move_number > 9:
            raise ValueError("Position must be between 1 and 9")

    def __validate_available_position(self, move_number):
        row: int = self.__players.__getitem__(self.__current_player).get_row()
        column: int = self.__players.__getitem__(self.__current_player).get_column()
        if self.__board[row][column] != " ":
            raise ValueError("Position already taken!")
