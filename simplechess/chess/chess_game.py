from simplechess.chess.chess_board import ChessBoard

from kivy.uix.relativelayout import RelativeLayout


class Chess(RelativeLayout):
    def __init__(self, **kwargs):
        super(Chess, self).__init__(**kwargs)
        self.board = ChessBoard()
        self.add_widget(self.board)

    def draw_pieces(self):
        self.board.draw_pieces(self.pieces)
