from chessPieces.board import Board
from chessPieces.knight import Knight
import sys, math, time

# Definitions

ALGORITHMS = [
  {
    "name": "A regra de Warnsdorff",
    "description": [
        "Algoritimo definitivo com heurística impecável",
        "Busca sempre o movimento de menor grau (sendo o grau, os caminhos possíveis incluindo os já visitados)",
        "Em casos genéricos, tem 100% de precisão, sem necessidade de retroceder"
      ],
    "method": "warnsdorffSearch"
  },
  {
    "name": "A regra de menor grau possível",
    "description":[
      "Seleciona o menor grau baseado somente no tabuleiro e não nos disponíveis",
      "Diferente de Warnsdorff, seleciona os movimentos possíveis do cavalo para a definição de grau",
      "Mas não inclui os caminhos já passados",
      "(Pode demorar em tabuleiros acima de tamanho 11)"
    ],
    "method": "leastDegree"
  },
  {
    "name": "Greedy-Search (Busca gulosa)",
    "description": [
      "Procura a solução até ser encontrada por força bruta",
      "(Até mesmo o tabuleiro padrão pode demorar com esse algoritimo)"
    ],
    "method": "bruteSearch"
  }
]

def algoTexts(simple = False):
  adjustment = max(len(algo["name"]) for algo in ALGORITHMS) + 2
  memo = ""

  for index, algo in enumerate(ALGORITHMS):
    name = algo["name"]
    description = ": " + '\n'.ljust(adjustment + 6, ' ').join(algo["description"]) if not simple else ""
    memo += f"{index + 1}- {name.ljust(adjustment, ' ')}{description}\n"

  return memo

def getAlgoRegex():
  return "^[" + ','.join([str(i + 1) for i in range(len(ALGORITHMS))]) + "]$"

sys.setrecursionlimit(3000)

# Helpers

def display(board, timer):
  if timer:
    board.exibit()
    time.sleep(timer)

def sumVectors(vec1, vec2):
  return [a + b for a,b in zip(vec1, vec2)]

# Sorting algos

def warnsdorff(board, coordinate):
  return len(Knight.possibleMovesForCoordinates(board, *coordinate))

def leastDegreeRule(board, coordinate):
  return len(Knight.possiblePlacesForCoordinates(board, *coordinate))

def sortSearch(knight, timer = None, sortAlgo= None):
  moves = knight.possibleMoves()
  if sortAlgo: moves.sort(key= lambda move: -sortAlgo(knight.board, sumVectors(knight.pos, move)))

  while moves:
    move = moves.pop()
    knight.move(*move)
    display(knight.board, timer)
    if knight.board.allDone() or sortSearch(knight, timer, sortAlgo): return knight.path()
    knight.rollback()
    display(knight.board, timer)

def dlSearch(knight, timer = None):
  moves = knight.possibleMoves()
  maxCases = knight.board.size ** 2

  while moves:
    move = moves.pop()
    knight.move(*move)
    display(knight.board, timer)
    if knight.board.allDone() or (knight.count < maxCases and sortSearch(knight, timer)): return knight.path()
    knight.rollback()
    display(knight.board, timer)

# Algo methods

def warnsdorffSearch(knight, timer = None):
  return sortSearch(knight, timer, sortAlgo= warnsdorff)

def leastDegree(knight, timer = None):
  return sortSearch(knight, timer, sortAlgo= leastDegreeRule)

def bruteSearch(knight, timer = None):
  return sortSearch(knight, timer, sortAlgo= None)

# Starters

def startSearch(size, pos, timer = 0, color = 0, algo = 0):
  newBoard = Board(size, color = color)
  newKnight = Knight(newBoard, *pos)
  algo = ALGORITHMS[algo]
  algoName = algo["name"]

  print("Iniciando algoritimo de busca")
  print("Variávies:")
  print(f"- Algoritimo: {algoName}")
  print(f"- Tamanho do tabuleiro: {size} X {size}")
  print(f"- Posição inicial do cavalo: {pos[0]}:{pos[1]}")
  print(f"- Com tempo entre os frames de {timer} segundos" if timer else "- Sem visualização")
  print()
  print("Iniciando em 3 segundos...:")
  time.sleep(3)
  print("Iniciado")

  moves = eval(algo["method"])(newKnight, timer)

  if not moves: return print("Não foi encontrado a solução")

  for index, move in enumerate(moves):
    newBoard.insert(*move, index)

  newBoard.exibit()