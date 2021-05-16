from .knight import Knight
import sys

class Board:
  BOARD_SIZE = 8
  SEPARATOR = '|'
  DEFAULT_EMPTY = 0

  def __init__(self, size = None):
    if not size: size = self.__class__.BOARD_SIZE
    empty = self.__class__.DEFAULT_EMPTY

    self.space = []
    for _ in range(size): self.space.append([empty] * size)

  def exibit(self):
    self.__printRow()

    separator = self.__class__.SEPARATOR
    lastIndex = self.__class__.BOARD_SIZE - 1

    for row in self.space:
      print(separator, end= '')
      for index, cell in enumerate(row):
        cellClass = type(cell) == Knight
        if cellClass: cell = cell.char()
        print(f' {str(cell).ljust(2, " ")} ', end= '')

        if index != lastIndex: print(separator, end= '')
      print(separator)

    self.__printRow()

  def insert(self, x, y, inserted = None):
    if inserted == None: inserted = self.__class__.DEFAULT_EMPTY

    self.space[y][x] = inserted

  def posAvailable(self, x, y):
    if not self.posExist(x, y): return False

    return self.space[y][x] == self.__class__.DEFAULT_EMPTY

  def posExist(self, x, y):
    for i in [x,y]:
      if i < 0 or i >= self.__class__.BOARD_SIZE: return False
    return True

  def allDone(self):
    symbol = self.__class__.DEFAULT_EMPTY
    for row in self.space:
      for cell in row:
        if cell == symbol: return False

    return True


  # Private

  def __printRow(self):
    print('-' * (len(self.space) * 5 + 1))