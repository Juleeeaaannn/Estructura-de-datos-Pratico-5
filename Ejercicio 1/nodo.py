from sympy import elliptic_e


class Nodo:
    __elemento=None
    __sig=None
    def __init__(self,elemento):
        self.__elemento=elemento
        self.__sig=None
    def setSig(self,elemento):
        self.__sig=elemento
    def getSig(self):
        return self.__sig
    def getElemento(self):
        return self.__elemento
    def setElemento(self,elemento):
        self.__elemento=elemento