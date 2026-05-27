from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB

a = ArvoreBB() 

c = int(input("Digite um elemento [-1 para sair]: "))
while c != -1:
  nome = input("Digite o nome do elemento: " )
  e = Elemento(c, nome)
  a.insere(e)
  #a.preOrdem(a.getRaiz())
  a.emOrdem(a.getRaiz())
  #a.posOrdem(a.getRaiz())
  c = int(input("Digite um elemento [-1 para sair]: "))

# Busca elementos
c = int(input("Digite um elemento [-1 para sair]: "))
while c != -1:
  no = a.remove(c)
  if no != None:
    print("Elemento encontrado: ", no.getValores())
    print("Árvore após remoção: ")
    a.emOrdem(a.getRaiz())
  else:
    print("Elemento não encontrado.")
  c = int(input("Digite um elemento [-1 para sair]: "))
