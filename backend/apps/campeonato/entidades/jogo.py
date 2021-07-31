class Jogo:
    def __init__(self, gols_casa, gols_visitante, clube_casa, clube_visitante, rodada, campeonato):
        self.__gols_casa = gols_casa
        self.__gols_visitante = gols_visitante
        self.__clube_casa = clube_casa
        self.__clube_visitante = clube_visitante
        self.__rodada = rodada
        self.__campeonato = campeonato

    @property
    def gols_casa(self):
        return self.__gols_casa

    @gols_casa.setter
    def gols_casa(self, gols_casa):
        self.__gols_casa = gols_casa

    @property
    def gols_visitante(self):
        return self.__gols_visitante

    @gols_visitante.setter
    def gols_visitante(self, gols_visitante):
        self.__gols_visitante = gols_visitante

    @property
    def clube_casa(self):
        return self.__clube_casa

    @clube_casa.setter
    def clube_casa(self, clube_casa):
        self.__clube_casa = clube_casa

    @property
    def clube_visitante(self):
        return self.__clube_visitante

    @clube_visitante.setter
    def clube_visitante(self, clube_visitante):
        self.__clube_visitante = clube_visitante

    @property
    def rodada(self):
        return self.__rodada

    @rodada.setter
    def rodada(self, rodada):
        self.__rodada = rodada

    @property
    def campeonato(self):
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato
