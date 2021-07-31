class Aposta:
    def __init__(self, usuario, campeonato, rodada):
        self.__usuario = usuario
        self.__rodada = rodada
        self.__campeonato = campeonato

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

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
