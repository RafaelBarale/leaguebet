class ApostaJogo:
    def __init__(self, gol_casa, gol_visitante, usuario, jogo):
        self.__gol_casa = gol_casa
        self.__gol_visitante = gol_visitante
        self.__usuario = usuario
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
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, jogo):
        self.__jogo = jogo
