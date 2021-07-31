class Campeonato:
    def __init__(self, nome, temporada):
        self.__nome = nome
        self.__temporada = temporada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def temporada(self):
        return self.__temporada

    @temporada.setter
    def temporada(self, temporada):
        self.__temporada = temporada

