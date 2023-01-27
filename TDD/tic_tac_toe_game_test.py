from unittest import TestCase

from tic_tac_toe_game.tic_tac_toe import TicTacToe


class TiccTacToeGameTest(TestCase):
    game: TicTacToe = TicTacToe()
    board: [] = game.get_board()
    game.register_player("Prof", 1)
    game.register_player("Ble", 2)
    game.take_position(1)
    first_player = game.get_players().__getitem__(0).get_symbol()

    def test_player_can_make_a_move_to_any_position_in_the_game_board(self) -> None:
        player_position: str = self.board.__getitem__(0).__getitem__(0)
        self.assertEqual(self.first_player, player_position)

    def test_two_players_can_play(self) -> None:
        self.game.take_position(9)
        second_player = self.game.get_players().__getitem__(1).get_symbol()
        player_1_position: str = self.board.__getitem__(0).__getitem__(0)
        self.assertEqual(self.first_player, player_1_position)
        player_2_position: str = self.board.__getitem__(2).__getitem__(2)
        self.assertEqual(second_player, player_2_position)

    def test_player_position_number_less_than_one_or_greater_than_9_raises_exception(self):
        with self.assertRaises(ValueError):
            self.game.take_position(37465)

    def test_that_position_already_taken_in_a_board_cannot_be_overriden_by_another_player(self):
        with self.assertRaises(ValueError):
            self.game.take_position(1)










if __name__ == '__main__':
    print("Hello world")