class Knight:
  MOVEMENTS = [[-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [2, -1], [1, 2], [2, 1]]
  PASSED = 'x'

  def __init__(self, board, x, y):
    self.pos = [x, y]
    self.board = board
    self.historic = []
    board.insert(x, y, inserted = self)

  def move(self, x, y):
    newPos = [i + j for i,j in zip(self.pos, [x, y])]

    self.board.insert(*self.pos, 'X')
    self.board.insert(*newPos, self)

    self.historic.append(self.pos)
    self.pos = newPos

  def possible_moves(self):
    moves = []
    for movement in self.__class__.MOVEMENTS:
      movement = [i + j for i,j in zip(movement, self.pos)]
      if self.board.posExist(*movement): moves.append(movement)

    return moves

  def char(self):
    return 'C'