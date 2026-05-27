from Elemento import Elemento
class NoABB: 
  def __init__(self, elemento = Elemento(), esq = None, dir = None):
    self.__dado = elemento
    self.__fe = esq
    self.__fd = dir
  def getDado(self):
    return self.__dado
  def setDado(self, e):
    self.__dado = e
  def getFE(self):
    return self.__fe
  def setFE(self, e):
    self.__fe = e
  def getFD(self):
    return self.__fd
  def setFD(self, d):
    self.__fd = d
  def getValores(self):
    return self.getDado().getValores()
  def eFolha(self):
    return self.getFE() == None and self.getFD() == None
  def temFilhoEsquerdo(self):
    return self.getFE() != None
  def temFilhoDireito(self):
    return self.getFD() != None
  def temDoisFilhos(self):
    return self.temFilhoEsquerdo() and self.temFilhoDireito()
  def eFilhoEsquerdo(self, pai):
    return pai.getFE() == self
  def eFilhoDireito(self, pai):
    return pai.getFD() == self
  def getChave(self):
    return self.getDado().getChave()