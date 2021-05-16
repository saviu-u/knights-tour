from searchAlgo import startSearch
import time

def expectInteger(phrase, quantity, standard = None, condition = None):
  return expectNumber(phrase, quantity, standard, condition, int)

def expectNumber(phrase, quantity, standard = None, condition = None, treat = float):
  while True:
    try:
      value = input(phrase + ": ")
      if standard != None and not value: return standard

      value = value.strip().split(" ")
      if len(value) != quantity: raise ValueError

      value = [treat(i) for i in value]
      if condition and not condition(value): raise ValueError

      return value if len(value) != 1 else value[0]
    except ValueError:
      print("Entrada inválida;\n")
      time.sleep(1)


print("Esse programa tem como finalidade;")
print("Mostrar o cavalo caminhando por todas as peças do campo")
print("Tudo foi feito abstraido em classes para melhor entendimento")
print()
print("TENHA CUIDADO")
print("O programa não mede uso de CPU ou memória")
print("Coloque valores altos por sua conta e risco")
print("------------------------------")
print("Grupo responsável pelo código: ")
for nome in ["Savio Cangussu", "Francisco Roque", "Guilherme Fernandes", "Raphael Bassi", "Gabriel Quaquio"]:
  print(" - ", nome)
print("------------------------------")
print()

while True:
  print("Defina;")
  boardSize = expectInteger("Tamanho do tabuleiro (EX: 10) (Padrão: 8)", 1, 8)
  knightPos = expectInteger("Posição inicial do cavalo (EX: 3 4) (Padrão: 0 0)", 2, [0, 0], lambda x: len([a for a in x if a >= 0 and a < boardSize]) == 2)
  timer = expectNumber("Tempo de intervalo para a observação do algoritimo em segundos (Digite 0 ou ENTER para nenhum)", 1, 0)

  print()

  startSearch(boardSize, knightPos, timer)

  print()
  if not expectInteger("Deseja tentar denovo (1 = Sim, 0 = Não) (Padrão: 0)", 1, 0): break
  print()





