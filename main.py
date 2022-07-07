from Pieces import *


class Board:
    def toString(self):
        text = [""] * 8
        for col in range(8):
            for row in range(8):
                if self.board[col][row].getPiece() is not None:
                    text[
                        row] += f"{type(self.board[col][row].getPiece()).__name__[:4]}({'W' if self.board[col][row].getPiece().isWhite() else 'B'}) "
                    # print piece types
                else:
                    text[row] += "[     ] "

                # text[row] += f"({self.board[col][row].getX()},{self.board[col][row].getY()}) "  # print tile coords
        return "\n".join(text)

    def __init__(self):
        self.board = [[Tile(col, row) for row in range(8)] for col in range(8)]
        self.newBoard()

    def newBoard(self):
        # white pieces:
        for col in range(8):
            self.board[col][6].setPiece(Pawn(True))
        self.board[0][7].setPiece(Rook(True))
        self.board[7][7].setPiece(Rook(True))
        self.board[1][7].setPiece(Knight(True))
        self.board[6][7].setPiece(Knight(True))
        self.board[2][7].setPiece(Bishop(True))
        self.board[5][7].setPiece(Bishop(True))
        self.board[4][7].setPiece(King(True))
        self.board[3][7].setPiece(Queen(True))

        # black pieces
        for col in range(8):
            self.board[col][1].setPiece(Pawn(False))
        self.board[0][0].setPiece(Rook(False))
        self.board[7][0].setPiece(Rook(False))
        self.board[1][0].setPiece(Knight(False))
        self.board[6][0].setPiece(Knight(False))
        self.board[2][0].setPiece(Bishop(False))
        self.board[5][0].setPiece(Bishop(False))
        self.board[4][0].setPiece(King(False))
        self.board[3][0].setPiece(Queen(False))


class Tile:

    def __init__(self, x, y, piece=None):
        self.piece = piece
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.getX()},{self.getY()})"

    def __repr__(self):
        return f"<Tile.({self.getX()},{self.getY()})>"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPiece(self):
        return self.piece

    def setPiece(self, piece):
        self.piece = piece

    def getValidMoves(self, board: Board):
        return [] if self.piece is None else self.piece.getValidMoves(board, self)


def printCoordBoard():
    text = [""] * 8
    for row in range(8):
        for col in range(8):
            text[row] += f"({col},{row}) "  # print tile coords
    return "\n".join(text)


if __name__ == '__main__':
    board = Board()
    print(board.toString())
    print(printCoordBoard())
    print(str(board.board[1][7].getValidMoves(board)))

    pass
