class Aposta:
    def __init__(self, usuario, rodada):
        self.__usuario = usuario
        self.__rodada = rodada

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

