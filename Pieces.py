from abc import ABC, abstractmethod
from main import Tile
from main import Board
from typing import List


class Piece(ABC):
    def __init__(self, white):
        self.white = white

    def isWhite(self):
        return self.white

    @abstractmethod
    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:  # TODO: add diagonal captures / en passant
        validTiles = []

        if self.isWhite():
            up1 = board.board[pos.getX()][pos.getY() - 1]
            up2 = board.board[pos.getX()][pos.getY() - 2]

            if up1.getPiece() is None:
                validTiles.append(up1)
                if pos.getY() == 6 and up2.getPiece() is None:
                    validTiles.append(up2)
        else:
            down1 = board.board[pos.getX()][pos.getY() + 1]
            down2 = board.board[pos.getX()][pos.getY() + 2]

            if down1.getPiece() is None:
                validTiles.append(down1)
                if pos.getY() == 1 and down2.getPiece() is None:
                    validTiles.append(down2)
        return validTiles


class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            while (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles += board.board[x][y]
                if board.board[x][y].getPiece().isWhite() != self.isWhite():
                    break
                x += direction[0]
                y += direction[1]

        return validTiles


class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass


class Bishop(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass


class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass


class King(Piece):
    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass
