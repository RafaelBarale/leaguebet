class Classificacao:
    #def __init__(self, pontos, jogos, vitorias, derrotas, empates, gols_pro, gols_contra, campeonato, clube):
    def __init__(self, campeonato, clube):
        self.__pontos = 0
        self.__jogos = 0
        self.__vitorias = 0
        self.__derrotas = 0
        self.__empates = 0
        self.__gols_pro = 0
        self.__gols_contra = 0
        self.__campeonato = campeonato
        self.__clube = clube

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

    @property
    def clube(self):
        return self.__clube

    @clube.setter
    def clube(self, clube):
        self.__clube = clube
