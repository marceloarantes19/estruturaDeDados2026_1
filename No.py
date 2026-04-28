from Elemento import Elemento
class No:
  def __init__(self, e = None):
    self.__dado = e
    self.__prox = None
  def getDado(self):
    return self.__dado 
  def setDado(self, elemento):
    self.__dado = elemento 
  def getProximo(self):
    return self.__prox
  def setProximo(self, p):
    self.__prox = p
  def getChave(self):
    return self.__dado.getChave()
  def setChave(self, c):
    self.__dado.setChave(c)
  def getNome(self):
    return self.getDado().getNome()
  def setNome(self, n):
    self.getDado().setNome(n)
  def getValores(self):
    return self.getDado().getValores()