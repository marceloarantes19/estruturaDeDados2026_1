from ListaEncadeada import ListaEncadeada
from No import No
from Elemento import Elemento
l = ListaEncadeada() 
while True:
  print("0  - Mostrar lista") 
  print("1  - Inserir no início")
  print("2  - Retirar do início")  
  print("3  - Inserir no fim")
  print("4  - Retirar do fim") 
  print("5  - Inserir ordenado")
  print("6  - Retirar pela chave")
  print("7  - Quantidade de elementos")
  print("-1 - Sair")
  op = int(input("Digite a opção: "))
  if op == -1:
    break
  elif op == 0:
    l.mostraLista() 
  elif op == 1 or op == 3 or op == 5:
    c = int(input("Digite a chave: "))
    nome = input("Digite o nome: ")
    e = Elemento(c, nome)
    no = No(e)
    if op == 1:
      l.insereNoInicio(no)
    elif op == 3:
      l.insereNoFim(no)
    else:
      l.insereOrdenado(no)
  elif op == 2 or op == 4:
    if not l.listaVazia():
      if op == 2:
        no = l.retiraNoInicio()
      else:
        no = l.retiraNoFim()
      print("Retirado: ", no.getValores())
    else:
      print("Lista Vazia")
  elif op == 6:
    c = int(input("Digite a chave a retirar: "))
    no = l.retiraPelaChave(c)
    if no != None:
      print("Retirado: ", no.getValores())
    else:
      print("Chave não encontrada")
  elif op == 7:
    print("Quantidade de elementos: ", l.quantidadeDeElementos())
