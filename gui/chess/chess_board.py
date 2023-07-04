from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.image import Image


class ChessBoard(Widget):
    def __init__(self, **kwargs):
        super(ChessBoard, self).__init__(**kwargs)
        self.board_texture = Image("assets/board_plain_01.png").texture
        self.board_texture.mag_filter = "nearest"
        self.board_texture.min_filter = "nearest"

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
