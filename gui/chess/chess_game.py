from chess.chess_board import ChessBoard

from kivy.uix.boxlayout import BoxLayout


class Chess(BoxLayout):
    def __init__(self, **kwargs):
        super(Chess, self).__init__(**kwargs)
        self.board = ChessBoard()
        self.add_widget(self.board)
