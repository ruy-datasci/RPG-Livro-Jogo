from dice.checks import Check

# Raça


class Raça:
    def __init__(self, nome, força, habilidade, pv_max, pm_max):
        Check.type_check(nome, str, 'nome')
        Check.type_check(força, int, 'força')
        Check.type_check(habilidade, int, 'habilidade')
        Check.type_check(pv_max, int, 'pv_max')
        Check.type_check(pv_max, int, 'pm_max')
        self._nome = nome
        self._for = força
        self._hab = habilidade
        self._pv_max = pv_max
        self._pm_max = pm_max

    def __repr__(self):
        return self._nome

    @property
    def nome(self):
        return self._nome

    @property
    def força(self):
        return self._for

    @property
    def habilidade(self):
        return self._hab

    @property
    def pv_max(self):
        return self._pv_max

    @property
    def pm_max(self):
        return self._pm_max


# Classes


class Classe:
    def __init__(self, nome, força, habilidade, pv_max, pm_max, vantagem):
        Check.type_check(nome, str, 'nome')
        Check.type_check(força, int, 'força')
        Check.type_check(habilidade, int, 'habilidade')
        Check.type_check(pv_max, int, 'pv_max')
        Check.type_check(pv_max, int, 'pm_max')
        Check.type_check(vantagem, str, 'pm_max')
        self._nome = nome
        self._for = força
        self._hab = habilidade
        self._pv_max = pv_max
        self._pm_max = pm_max
        self._vantagem = vantagem.lower()

    def __repr__(self):
        return self._nome

    @property
    def nome(self):
        return self._nome

    @property
    def força(self):
        return self._for

    @property
    def habilidade(self):
        return self._hab

    @property
    def pv_max(self):
        return self._pv_max

    @property
    def pm_max(self):
        return self._pm_max

    @property
    def vantagem(self):
        return self._vantagem


class Vantagens(type):
    def __str__(self): return f'{self._nome.title()}'

    def executar(self, combate): pass

    def reset(self): pass


class Item:
    def __init__(self, nome, força=0):
        self.nome = nome
        self.força = força

    def __repr__(self):
        return str(self.nome)


class Mochila:
    def __init__(self):
        self.mochila = {}
        self.equipamentos = {}


class Carteira:
    def __init__(self):
        self.dinheiro = 0
