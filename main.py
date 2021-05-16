from chessPieces.board import Board
from chessPieces.knight import Knight
import sys

sys.setrecursionlimit(3000)
print("começa")
newBoard = Board()
newKnight = Knight(newBoard, 0, 0)

def search(knight):
  if knight.board.allDone(): return knight.historic

  moves = []
  moves = knight.possibleMoves()

  while moves:
    move = moves.pop()
    knight.move(*move)
    newBoard.exibit()
    search(knight)
    knight.rollback()
    newBoard.exibit()

if search(newKnight): print(newKnight.historic)