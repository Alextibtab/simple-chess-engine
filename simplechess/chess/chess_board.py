import simplechess.utils.fen as fen
from simplechess.chess.chess_engine.piece import Piece
from simplechess.chess.chess_piece import ChessPiece

from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color
from kivy.core.image import Image as CoreImage

piece_texture_path = {
    Piece.PAWN: "Pawn.png",
    Piece.KNIGHT: "Knight.png",
    Piece.BISHOP: "Bishop.png",
    Piece.ROOK: "Rook.png",
    Piece.QUEEN: "Queen.png",
    Piece.KING: "King.png",
}


class ChessBoard(RelativeLayout):
    def __init__(self, **kwargs):
        super(ChessBoard, self).__init__(**kwargs)
        self.board_texture = CoreImage("simplechess/assets/board_plain_01.png").texture
        self.board_texture.mag_filter = "nearest"
        self.board_texture.min_filter = "nearest"
        self.pieces = [None] * 64
        self.draw_board()
        self.init_pieces(self.pieces)

    def on_size(self, *args):
        self.canvas.clear()
        self.draw_board()

    def draw_board(self):
        with self.canvas:
            self.board = Rectangle(
                pos=(self.width / 2 - self.height / 2, self.y),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size=(self.height, self.height),
                texture=self.board_texture,
            )

    def draw_piece(self, index, piece):
        color = "W_" if piece & Piece.WHITE else "B_"
        if color == "W_":
            piece -= Piece.WHITE
        else:
            piece -= Piece.BLACK
        piece = piece_texture_path[piece]
        piece_texture = CoreImage("simplechess/assets/" + color + piece).texture
        self.add_widget(
            ChessPiece(piece_texture, self.index_to_square(index)),
            index=index,
            canvas="after",
        )

    def draw_pieces(self, pieces):
        for idx, piece in enumerate(pieces):
            if piece != Piece.NONE:
                self.draw_piece(idx, piece)

    def init_pieces(self, pieces):
        fen.fill_array_from_fen(pieces, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        self.draw_pieces(pieces)

    def index_to_square(self, index):
        return (index % 8, index // 8)
