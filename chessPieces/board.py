from .knight import Knight
import sys

class Board:
  BOARD_SIZE = 8
  SEPARATOR = '|'
  DEFAULT_EMPTY = '0'
  COLOR_DICT = {
    "Knight": '\033[31;44m',
    'X': '\033[30;42m',
    '0': '\033[37;47m'
  }

  DEFAULT_COLOR = '\033[m'
  DEFAULT_SPECIAL_PIECE_COLOR = '\033[31;47m'


  def __init__(self, size = None, color = 0):
    if not size: size = self.__class__.BOARD_SIZE

    self.size = size
    self.space = []
    self.color = color

    for _ in range(size): self.space.append([self.__class__.DEFAULT_EMPTY] * size)

  def exibit(self):
    self.__printRow()

    separator = self.__class__.SEPARATOR
    lastIndex = self.size - 1
    colorDict = self.__class__.COLOR_DICT

    for row in self.space:
      print(separator, end= '')
      for index, cell in enumerate(row):
        cellClass = type(cell) == Knight
        keyColor = type(cell).__name__ if cellClass else cell
        prefix = sufix = ''

        if cellClass: cell = cell.char()

        if self.color:
          try:
            prefix = colorDict[keyColor]
            sufix = self.__class__.DEFAULT_COLOR
          except KeyError:
            prefix = sufix = ''

        print(prefix + f' {str(cell).ljust(2, " ")} ' + sufix, end= '')

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
      if i < 0 or i >= self.size: return False
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