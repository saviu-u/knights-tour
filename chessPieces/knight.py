class Knight:
  MOVEMENTS = [[-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [2, -1], [1, 2], [2, 1]]
  PASSED = 'X'

  def __init__(self, board, x, y):
    self.pos = [x, y]
    self.board = board
    self.historic = [[x, y]]
    board.insert(x, y, inserted = self)

  @classmethod
  def possibleMovesForCoordinates(cls, board, x, y):
    moves = []
    for movement in cls.MOVEMENTS:
      position = [i + j for i,j in zip(movement, [x, y])]
      if board.posAvailable(*position): moves.append(movement)

    return moves

  @classmethod
  def possiblePlacesForCoordinates(cls, board, x, y):
    moves = []
    for movement in cls.MOVEMENTS:
      position = [i + j for i,j in zip(movement, [x, y])]
      if board.posExist(*position): moves.append(movement)

    return moves

  def path(self):
    return self.historic + [self.pos]

  def move(self, x, y):
    newPos = [i + j for i,j in zip(self.pos, [x, y])]

    self.board.insert(*self.pos, self.__class__.PASSED)
    self.board.insert(*newPos, self)

    self.historic.append(self.pos)
    self.pos = newPos

  def rollback(self):
    self.board.insert(*self.pos)
    self.pos = self.historic.pop()
    self.board.insert(*self.pos, self)

  def possibleMoves(self):
    return self.__class__.possibleMovesForCoordinates(self.board, *self.pos)

  def char(self):
    return 'C'