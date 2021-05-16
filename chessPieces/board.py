from .knight import Knight

class Board:
  BOARD_SIZE = 8
  SEPARATOR = '|'
  DEFAULT_EMPTY = 0

  def __init__(self):
    size = self.__class__.BOARD_SIZE
    empty = self.__class__.DEFAULT_EMPTY

    self.space = []
    for _ in range(8): self.space.append([empty] * size)

  def exibit(self):
    self.__printRow()

    separator = self.__class__.SEPARATOR
    lastIndex = self.__class__.BOARD_SIZE - 1

    for row in self.space:
      print(separator, end= '')
      for index, cell in enumerate(row):
        if type(cell) == Knight: cell = cell.char()
        print(f' {cell} ', end= '')
        if index != lastIndex: print(separator, end= '')
      print(separator)

    self.__printRow()

  def insert(self, x, y, inserted = None):
    if inserted == None: inserted = self.__class__.DEFAULT_EMPTY

    self.space[x][y] = inserted

  def posAvailable(self, x, y):
    if not self.posExist(x, y): return False

    return self.space[x][y] == self.__class__.DEFAULT_EMPTY

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
    print('-' * (len(self.space) * 4 + 1))