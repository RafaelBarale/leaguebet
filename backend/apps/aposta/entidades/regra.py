class Regra:
    def __init__(self, campeonato, vencedor, golCasa, golVisitante):
        self.__campeonato = campeonato
        self.__vencedor = vencedor
        self.__golCasa = golCasa
        self.__golVisitante = golVisitante

    @property
    def campeonato(self):
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato

    @property
    def vencedor(self):
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self.__vencedor = vencedor

    @property
    def golCasa(self):
        return self.__golCasa

    @golCasa.setter
    def golCasa(self, golCasa):
        self.__golCasa = golCasa

    @property
    def golVisitante(self):
        return self.__golVisitante

    @golVisitante.setter
    def golVisitante(self, golVisitante):
        self.__golVisitante = golVisitante
