from searchAlgo import algoTexts, startSearch, getAlgoRegex, ALGORITHMS
import time
import re

def expectInteger(phrase, regex, standard = None, condition = None):
  return expectNumber(phrase, regex, standard, condition, int)

def expectNumber(phrase, regex, standard = None, condition = None, treat = float):
  while True:
    try:
      value = input(phrase + ": ")
      if standard != None and not value: return standard

      if not re.search(regex, value): raise ValueError
      value = value.strip().split(" ")

      value = [treat(i) for i in value]
      if condition and not condition(value): raise ValueError

      return value if len(value) != 1 else value[0]
    except ValueError:
      print("Entrada inválida;\n")
      time.sleep(1)

print("------------------------------------------------------------------------------------------")
print("Esse programa tem como finalidade;")
print("Mostrar o cavalo caminhando por todas as peças do campo uma só vez")
print("Tudo foi feito abstraido em classes para melhor entendimento")
print()
print("TENHA CUIDADO")
print("O programa não mede uso de CPU ou memória")
print("A linguagem python não lida bem com alto uso de memória")
print("e pode fechar o programa sozinho dependendo da ordenação escolhida")
print()
print("------------------------------------------------------------------------------------------")
print()
print(f"Para intuito desse trabalho, serão disponibilizados {len(ALGORITHMS)} algoritmos para busca")
print("Ordenados respectivamente pela ordem de provavél eficiência")
print()
print(algoTexts())
print("------------------------------------------------------------------------------------------")
print("Grupo responsável pelo código: ")
for nome in ["Savio Cangussu", "Francisco Roque", "Guilherme Fernandes", "Raphael Bassi", "Gabriel Quaquio"]:
  print(" - ", nome)
print("------------------------------------------------------------------------------------------")
print()
print("Primeiramente..")
print("O Comand Prompt do windows (CMD) NÃO aceita cor nativamente, sabendo disso;")

# Start inputs
try:
  enableColor = expectInteger("O seu terminal aceita cores no STDOUT (1 = Sim, 0 = Não) (Padrão: 0)", r"^[0,1]$", 0)
  print()
except KeyboardInterrupt:
  exit()

while True:
  try:
    print("Defina;")

    boardSize = expectInteger("Tamanho do tabuleiro (EX: 5) (Padrão: 8)", r"^\d+$", 8)
    knightPos = expectInteger("Posição inicial do cavalo (EX: 3 4) (Padrão: 0 0)", r"^\d+ \d+$", [0, 0], lambda x: len([a for a in x if a >= 0 and a < boardSize]) == 2)
    algo = expectInteger("Dos algoritmos:\n" + algoTexts(simple= True) + "Qual algoritimo quer usar? (Padrão: 1)", getAlgoRegex(), 1) - 1
    timer = expectInteger("Frames por segundo para exibição do algoritimo (Digite 0 ou ENTER para nenhum)", r"^\d+", 0)
    if timer: timer = 1/timer

    print()
    startSearch(boardSize, knightPos, timer, enableColor, algo)
    print()
  except KeyboardInterrupt:
    print("\n\n")

  try:
    if not expectInteger("Deseja tentar denovo (1 = Sim, 0 = Não) (Padrão: 0)", r"^[0,1]$", 0): break
    print()
  except KeyboardInterrupt:
    exit()





