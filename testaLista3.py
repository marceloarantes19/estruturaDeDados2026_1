from Elemento import Elemento
from No import No 
from ListaEncadeada import ListaEncadeada 

l = ListaEncadeada()
c = int(input("Digite a chave [-1 para sair]: "))
while c != -1:
  nome = input("Digite o Nome: ")
  e = Elemento(c, nome)
  no = No(e)
  l.insereOrdenado(no)
  print("Lista Atual: ")
  l.mostraLista()
  c = int(input("\nDigite a chave [-1 para sair]: "))

c = int(input("\nDigite a chave a sair [-1 para terminar]: "))
while not l.listaVazia() and c != -1:
  no = l.retiraPelaChave(c)
  if no != None:
    print(no.getValores(), "Removido")
  l.mostraLista()
  c = int(input("\nDigite a chave a sair [-1 para terminar]: "))
