from Elemento import Elemento
from No import No 
from ListaEncadeada import ListaEncadeada 

l = ListaEncadeada()
c = int(input("Digite a chave [-1 para sair]: "))
while c != -1:
  nome = input("Digite o Nome: ")
  e = Elemento(c, nome)
  no = No(e)
  l.insereNoFim(no)
  print("Lista Atual: ")
  l.mostraLista()
  c = int(input("\nDigite a chave [-1 para sair]: "))

while not l.listaVazia():
  print(l.retiraNoFim().getValores())

