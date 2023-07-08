from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class ChessPiece(Widget):
    def __init__(self, texture, position, **kwargs):
        super(ChessPiece, self).__init__(**kwargs)
        self.piece_texture = texture
        self.board_position = position
        self.piece_texture.mag_filter = "nearest"
        self.piece_texture.min_filter = "nearest"
        self.draw_piece()

    def on_size(self, *args):
        self.canvas.clear()
        self.draw_piece()

    def draw_piece(self):
        with self.canvas:
            self.piece = Rectangle(
                pos=(self.x, self.y),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size=(16, 32),
                texture=self.piece_texture,
            )
