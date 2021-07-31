class Clube:
    def __init__(self, nome, nome_abreviado, estado, escudo):
        self.__nome = nome
        self.__nome_abreviado = nome_abreviado
        self.__estado = estado
        self.__escudo = escudo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nome_abreviado(self):
        return self.__nome_abreviado

    @nome_abreviado.setter
    def nome_abreviado(self, nome_abreviado):
        self.__nome_abreviado = nome_abreviado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
