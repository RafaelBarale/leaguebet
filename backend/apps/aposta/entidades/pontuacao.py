class Pontuacao:
    def __init__(self, campeonato, usuario, pontos):
        self.__campeonato = campeonato
        self.__usuario = usuario
        self.__pontos = pontos

    @property
    def campeonato(self):
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

