from simplechess.chess.chess_engine.piece import Piece

PIECES = {
    "K": Piece.WHITE | Piece.KING,
    "Q": Piece.WHITE | Piece.QUEEN,
    "R": Piece.WHITE | Piece.ROOK,
    "B": Piece.WHITE | Piece.BISHOP,
    "N": Piece.WHITE | Piece.KNIGHT,
    "P": Piece.WHITE | Piece.PAWN,
    "k": Piece.BLACK | Piece.KING,
    "q": Piece.BLACK | Piece.QUEEN,
    "r": Piece.BLACK | Piece.ROOK,
    "b": Piece.BLACK | Piece.BISHOP,
    "n": Piece.BLACK | Piece.KNIGHT,
    "p": Piece.BLACK | Piece.PAWN,
}

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def create_array_from_fen(fen):
    pieces = [Piece.NONE] * 64
    fen = fen.split("/")
    for i in range(len(fen)):
        row = fen[i]
        column = 0
        for j in range(len(row)):
            if row[j].isdigit():
                for k in range(int(row[j])):
                    pieces[i * 8 + column] = Piece.NONE
                    column += 1
            else:
                pieces[i * 8 + column] = PIECES[row[j]]
                column += 1
    return pieces
