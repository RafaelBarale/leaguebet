class Classificacao:
    def __init__(self, pontos, jogos, vitorias, derrotas, empates, gols_pro, gols_contra, campeonato):
        self.__pontos = pontos
        self.__jogos = jogos
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empates = empates
        self.__gols_pro = gols_pro
        self.__gols_contra = gols_contra
        self.__campeonato = campeonato

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @property
    def jogos(self):
        return self.__jogos

    @jogos.setter
    def jogos(self, jogos):
        self.__jogos = jogos

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, vitorias):
        self.__vitorias = vitorias

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, derrotas):
        self.__derrotas = derrotas

    @property
    def empates(self):
        return self.__empates

    @empates.setter
    def empates(self, empates):
        self.__empates = empates

    @property
    def gols_pro(self):
        return self.__gols_pro

    @gols_pro.setter
    def gols_pro(self, gols_pro):
        self.__gols_pro = gols_pro

    @property
    def gols_contra(self):
        return self.__gols_contra

    @gols_contra.setter
    def gols_contra(self, gols_contra):
        self.__gols_contra = gols_contra

    @property
    def campeonato(self):
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, campeonato):
        self.__campeonato = campeonato
