from chessPieces.board import Board
from chessPieces.knight import Knight

newBoard = Board()
newKnight = Knight(newBoard, 1, 1)

newBoard.exibit()
print(newKnight.possible_moves())