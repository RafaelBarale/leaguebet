class Rodada:
    def __init__(self, numero, campeonato, fechada):
        self.__numero = numero
        self.__campeonato = campeonato
        self.__fechada = fechada

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def campeonato(self):
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato

    @property
    def fechada(self):
        return self.__fechada

    @fechada.setter
    def fechada(self, fechada):
        self.__fechada = fechada