from chessPieces.board import Board
from chessPieces.knight import Knight
import sys, math, time

sys.setrecursionlimit(3000)

def display(board, timer):
  if timer:
    board.exibit()
    time.sleep(timer)

def sortMoves(knight, coordinate):
  return (-warnsdorffs(knight, coordinate))

def warnsdorffs(knight, coordinate):
  pos = [a + b for a,b in zip(knight.pos, coordinate)]
  return len(Knight.possiblePlacesForCoordinates(knight.board, *pos))

def search(knight, timer = None):
  moves = []
  moves = knight.possibleMoves()
  moves.sort(key= lambda x: sortMoves(knight, x))

  while moves:
    move = moves.pop()
    knight.move(*move)
    display(knight.board, timer)
    if knight.board.allDone() or search(knight, timer): return knight.path()
    knight.rollback()
    display(knight.board, timer)

def startSearch(size, pos, timer = 0, color = 0):
  newBoard = Board(size, color = color)
  newKnight = Knight(newBoard, *pos)

  moves = search(newKnight, timer)

  if not moves: return print("Não foi encontrado a solução")

  for index, move in enumerate(moves):
    newBoard.insert(*move, index)

  newBoard.exibit()