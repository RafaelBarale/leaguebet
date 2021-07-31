class Aposta:
    def __init__(self, gol_casa, gol_visitante, aposta, jogo):
        self.__gol_casa = gol_casa
        self.__gol_visitante = gol_visitante
        self.__aposta = aposta
        self.__jogo = jogo

    @property
    def gol_casa(self):
        return self.__gol_casa

    @gol_casa.setter
    def gol_casa(self, gol_casa):
        self.__gol_casa = gol_casa

    @property
    def gol_visitante(self):
        return self.__gol_visitante

    @gol_visitante.setter
    def gol_visitante(self, gol_visitante):
        self.__gol_visitante = gol_visitante

    @property
    def aposta(self):
        return self.__aposta

    @aposta.setter
    def aposta(self, aposta):
        self.__aposta = aposta

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def aposta(self, jogo):
        self.__jogo = jogo
