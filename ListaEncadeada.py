from No import No
class ListaEncadeada:
  def __init__(self):
    self.__cabeca = No()
  def listaVazia(self):
    return self.__cabeca.getProximo() == None
  def insereNoInicio(self, no):
    no.setProximo(self.__cabeca.getProximo())
    self.__cabeca.setProximo(no) 
  def retiraNoInicio(self):
    ret = None 
    if not self.listaVazia():
      ret = self.__cabeca.getProximo()
      self.__cabeca.setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret
  def insereNoFim(self, no):
    ant = self.__cabeca
    atu = ant.getProximo()
    while atu != None:
      ant = atu 
      atu = atu.getProximo()
    ant.setProximo(no)
  def retiraNoFim(self):
    atu = self.__cabeca.getProximo()
    if not self.listaVazia():
      ant = self.__cabeca
      while atu.getProximo() != None:
        ant = atu 
        atu = ant.getProximo()
      ant.setProximo(None)
    return atu
  def insereOrdenado(self, no):
    ant = self.__cabeca
    atu = ant.getProximo()
    while atu != None and no.getChave() > atu.getChave():
      ant = atu 
      atu = atu.getProximo()
    no.setProximo(atu)
    ant.setProximo(no)
  def retiraPelaChave(self, chave):
    ant = self.__cabeca
    atu = ant.getProximo()
    while atu != None and atu.getChave() != chave:
      ant = atu
      atu = atu.getProximo()
    if atu != None:
      ant.setProximo(atu.getProximo())
      atu.setProximo(None)
    return atu

  def mostraLista(self):
    atual = self.__cabeca.getProximo()
    while atual != None:
      print(atual.getValores())
      atual = atual.getProximo()

# Exercício 3: Quantidade de elementos na lista
def quantidadeDeElementos(self):
  qtd = 0
  atual = self.__cabeca.getProximo()
  while atual != None:
    qtd = qtd + 1
    atual = atual.getProximo() 
  return qtd
