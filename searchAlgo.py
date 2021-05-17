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

  print("Iniciando algoritimo de busca")
  print("Heurísticas usadas: Regra de Warnsdorffs")
  print("Variávies:")
  print(f"- Tamanho do tabuleiro: {size} X {size}")
  print(f"- Posição inicial do cavalo: {pos[0]}:{pos[1]}")
  print(f"- Com tempo entre as jogas de {timer} segundos" if timer else "- Sem visualização")
  print()

  if size >= 10:
    print("AVISO")
    print("Testes foram feitos com tabuleiros acima de tamanho 11 e a busca costuma demorar")
  print("Iniciando em 3 segundos...:")
  time.sleep(3)
  print("Iniciado")

  moves = search(newKnight, timer)

  if not moves: return print("Não foi encontrado a solução")

  for index, move in enumerate(moves):
    newBoard.insert(*move, index)

  newBoard.exibit()