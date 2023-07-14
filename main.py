from re import X
import simplechess.utils.fen as fen
from simplechess.chess.chess_engine.piece import Piece

import cProfile

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.uix.image import Image
from kivy.properties import (
    StringProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ListProperty,
    ObjectProperty,
)


class Chess(RelativeLayout):
    Board = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Chess, self).__init__(**kwargs)
        self.Board = ChessBoard()
        self.add_widget(self.Board)


class ChessBoard(RelativeLayout):
    piece_layout = ObjectProperty(None)
    background = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ChessBoard, self).__init__(**kwargs)
        self.background = ChessBoardImage()
        self.add_widget(self.background)
        self.piece_layout = ChessPieceLayout()
        self.add_widget(self.piece_layout)


class ChessBoardImage(Image):
    board_theme = StringProperty("board_plain_03")

    def on_texture(self, *args):
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"


class ChessPieceLayout(RelativeLayout):
    selected_piece = ObjectProperty(None)
    pieces = ListProperty(None)

    def __init__(self, **kwargs):
        super(ChessPieceLayout, self).__init__(**kwargs)
        self.pieces = fen.create_array_from_fen(fen.STARTING_FEN)
        self.init_pieces()

    def init_pieces(self):
        for index, piece in enumerate(self.pieces):
            self.add_piece(piece, index)

    def add_piece(self, piece, index):
        rank, file = self.index_to_rank_file(index)
        if piece & Piece.WHITE:
            colour = "white"
            piece -= Piece.WHITE
        else:
            colour = "black"
            piece -= Piece.BLACK
        match piece:
            case Piece.KING:
                self.add_widget(
                    ChessPiece(piece="King", colour=colour, rank=rank, file=file)
                )
            case Piece.QUEEN:
                self.add_widget(
                    ChessPiece(piece="Queen", colour=colour, rank=rank, file=file)
                )
            case Piece.ROOK:
                self.add_widget(
                    ChessPiece(piece="Rook", colour=colour, rank=rank, file=file)
                )
            case Piece.BISHOP:
                self.add_widget(
                    ChessPiece(piece="Bishop", colour=colour, rank=rank, file=file)
                )
            case Piece.KNIGHT:
                self.add_widget(
                    ChessPiece(piece="Knight", colour=colour, rank=rank, file=file)
                )
            case Piece.PAWN:
                self.add_widget(
                    ChessPiece(piece="Pawn", colour=colour, rank=rank, file=file)
                )

    def index_to_rank_file(self, index):
        return index // 8, index % 8

    def on_selected_piece(self, *args):
        print(self.selected_piece)

    def on_touch_down(self, touch):
        file, rank = self.get_file_and_rank(touch.pos)
        if self.selected_piece:
            self.selected_piece.move(file, rank)
            self.selected_piece.moved()
            self.selected_piece = None
        return True

    def get_file_and_rank(self, pos):
        square_size = self.width / 8
        widget_pos = self.to_widget(*pos)
        return (widget_pos[0] // square_size, pos[1] // square_size)


class ChessPiece(Image):
    selected = BooleanProperty(False)
    colour = StringProperty("white")
    piece = StringProperty("King")
    rank = BoundedNumericProperty(0, min=0, max=7)
    file = BoundedNumericProperty(0, min=0, max=7)

    def on_texture(self, *args):
        self.texture.mag_filter = "nearest"
        self.texture.min_filter = "nearest"

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.selected = True
            self.parent.selected_piece = self
            return True
        else:
            return super().on_touch_down(touch)

    def move(self, file, rank):
        self.rank = rank
        self.file = file

    def moved(self):
        self.selected = False


class MenuScreen(Screen):
    pass


class PlayerVsPlayerScreen(Screen):
    pass


class PlayerVsComputerScreen(Screen):
    pass


class ComputerVsComputerScreen(Screen):
    pass


class ChessApp(App):
    def on_start(self):
        self.profile = cProfile.Profile()
        self.profile.enable()

    def on_stop(self):
        self.profile.disable()
        self.profile.dump_stats("chess_app.profile")

    def build(self):
        self.settings_cls = SettingsWithTabbedPanel
        self.icon = "simplechess/assets/W_King.png"

        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(PlayerVsPlayerScreen(name="player_vs_player"))
        self.sm.add_widget(PlayerVsComputerScreen(name="player_vs_ai"))
        self.sm.add_widget(ComputerVsComputerScreen(name="ai_vs_ai"))

        return self.sm

    def build_config(self, config):
        config.read("config.ini")

    def display_settings(self, settings):
        if not self.sm.has_screen("settings"):
            s = Screen(name="settings")
            s.add_widget(settings)
            self.sm.add_widget(s)
        self.sm.transition.direction = "left"
        self.sm.current = "settings"

    def build_settings(self, settings):
        settings.add_json_panel("Chess", self.config, "settings.json")

    def close_settings(self, *largs):
        if self.sm.current == "settings":
            self.sm.transition.direction = "right"
            self.sm.current = "menu"


if __name__ == "__main__":
    ChessApp().run()
