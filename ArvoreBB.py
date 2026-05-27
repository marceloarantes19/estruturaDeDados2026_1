from Elemento import Elemento
from NoABB import NoABB 
class ArvoreBB:
  def __init__(self):
    self.__raiz = None
  def getRaiz(self):
    return self.__raiz
  def setRaiz(self, r):
    self.__raiz = r
  def estaVazia(self):
    return self.getRaiz() == None
  # Cria um nó a partir de um elemento
  def criaNo(self, elemento):
    return NoABB(elemento)
  
  # Insere um elemento na raiz ou chama o método recursivo de inserção
  def insere(self, elemento):
    no = self.criaNo(elemento)
    if self.estaVazia():
      self.setRaiz(no)
    else:
      self.__insere(self.getRaiz(), no)
  
  # Método recursivo de inserção
  def __insere(self, pai, no):
    if no.getChave() < pai.getChave():
      if pai.getFE() == None:
        pai.setFE(no)
      else:
        self.__insere(pai.getFE(), no)
    else:
      if pai.getFD() == None:
        pai.setFD(no)
      else:
        self.__insere(pai.getFD(), no)
  
  # Passeio pre ordem
  def preOrdem(self, no):
    if no != None:
      print(no.getValores())
      self.preOrdem(no.getFE())
      self.preOrdem(no.getFD()) 
  
  # Passeio em ordem
  def emOrdem(self, no):  
    if no != None:
      self.emOrdem(no.getFE())
      print(no.getValores())
      self.emOrdem(no.getFD())

  # Passeio pos ordem
  def posOrdem(self, no): 
    if no != None:
      self.posOrdem(no.getFE())
      self.posOrdem(no.getFD())
      print(no.getValores()) 
  
  # Busca um elemento a partir de sua chave
  def busca(self, chave):
    return self.__busca(self.getRaiz(), chave)
  def __busca(self, no, chave):
    if no == None:
      return None
    elif no.getChave() == chave:
      return no
    elif chave < no.getChave():
      return self.__busca(no.getFE(), chave)
    else:
      return self.__busca(no.getFD(), chave)


  # Verificar a remoção ...
  def remove(self, chave):
    self.setRaiz(self.__remove(None, self.getRaiz(), chave))  
  def __remove(self, pai, no, chave):
    if no == None:
      return None
    elif chave < no.getChave():
      no.setFE(self.__remove(no, no.getFE(), chave))
    elif chave > no.getChave():
      no.setFD(self.__remove(no, no.getFD(), chave))
    else: # nó encontrado
      if not no.temDoisFilhos():
        if no.eFolha():
          if pai == None: # nó é a raiz
            self.setRaiz(None)
          elif no.eFilhoEsquerdo(pai):
            pai.setFE(None)
          else:
            pai.setFD(None)
        elif no.temFilhoEsquerdo():
          if pai == None: # nó é a raiz
            self.setRaiz(no.getFE())
          elif no.eFilhoEsquerdo(pai):
            pai.setFE(no.getFE())
          else:
            pai.setFD(no.getFE())
          no.setFE(None)
        elif no.temFilhoDireito():
          if pai == None: # nó é a raiz
            self.setRaiz(no.getFD())
          elif no.eFilhoEsquerdo(pai):
            pai.setFE(no.getFD())
          else:
            pai.setFD(no.getFD())
          no.setFD(None)
        return no
      else: # nó tem dois filhos
        return self.__removeNoComDoisFilhos(no, no, no.getFE())
  def __removeNoComDoisFilhos(self, noASerRemovido, pai, no):
    if no.getFD() != None:
      return self.__removeNoComDoisFilhos(noASerRemovido, no, no.getFD())
    else:
      dado = noASerRemovido.getDado()
      noASerRemovido.setDado(no.getDado())
      if pai == noASerRemovido:
        pai.setFE(no.getFE())
      else:
        pai.setFD(no.getFE())
      no.setFE(None)
      return no