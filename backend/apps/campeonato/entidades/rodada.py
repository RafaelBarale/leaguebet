class Rodada:
    def __init__(self, numero, campeonato):
        self.__numero = numero
        self.__campeonato = campeonato

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
