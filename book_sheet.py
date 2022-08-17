# -*- coding : utf-8 -*-
from dice.dice_bag import RpgRoller as DiceBag
from dice.livro_jogo.regras.regras import Regras
from dice.livro_jogo.core import Seletor
from dice.livro_jogo.regras.core import Mochila,Carteira


class Personagem:
    def __init__(self, nome, raça=None, classe=None):
        self._name = nome.title()
        self._race = Seletor.selecionar(Regras.races) if (raça is None) else raça
        self._class = Seletor.selecionar(Regras.classes) if (classe is None) else classe
        self._pv_max = self._race.pv_max+self._class.pv_max
        self._pv = self._pv_max
        self._pm_max = self._race.pm_max+self._class.pm_max
        self._pm = self._pm_max
        self._hab = self._race.habilidade+self._class.habilidade
        self._for = self._race.força+self._class.força
        self.mochila = Mochila()
        self.carteira = Carteira()
        self._vantagens = {}
        self._vantagens.update(self._class.vantagem)
        self._pontos = 3
        self._aplicar_pontos()


    def __repr__(self):
        return f'''\
Nome: {self._name}
Raça: {self._race}
Classe: {self._class}
Pv: {self._pv}/{self._pv_max}
Pm: {self._pm}/{self._pm_max}
Força: {self._for}
Habilidade: {self._hab}
Vantagens: {set(self._vantagens)}
Mochila: {self.mochila}
Carteira: {self.carteira}'''

    @property
    def pv(self):
        return self._pv

    @property
    def pm(self):
        return self._pm

    @property
    def força(self):
        return self._for

    @property
    def habilidade(self):
        return self._hab

    @property
    def vantagens(self):
        return self._vantagens

    def d_pv(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._pv += valor
            self._pv = min(self._pv, self._pv_max)
            self._pv = max(self._pv, 0)
        return self

    def d_pm(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._pm += valor
            self._pm = max(self._pm, 0)
            self._pm = min(self._pm, self._pm_max)
        return self

    def _d_pv_max(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._pv_max += valor
            self._pv_max = max(1, self._pv_max)
            self._pv = min(self._pv, self._pv_max)
        return self

    def _d_pm_max(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._pm_max += valor
            self._pm_max = max(1, self._pm_max)
            self._pm = min(self._pm, self._pm_max)
        return self

    def _d_forca(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._for += valor
            self._for = max(0, self._for)
        return self

    def _d_hab(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._hab += valor
            self._hab = max(0, self._hab)
        return self

    def _d_pontos(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor deve ser in Inteiro')
        else:
            self._pontos += valor
        return self

    def _add_vantagem(self):
        vantagem = Seletor.selecionar(Regras.vantagens, self._vantagens)
        if vantagem != False:
            self._vantagens.update({str(vantagem): vantagem})
        else:
            self._d_pontos(1)
        return self

    def _aplicar_pontos(self):
        while self._pontos > 0:
            print(self)
            print(f'Pontos restantes: {self._pontos}')
            Seletor.selecionar(Regras.opcoes_pontos)(self)

    @staticmethod
    def roll(die=2, bonus=0):
        res = DiceBag.roll(die, 6, bonus)
        return res


class Criatura:
    def __init__(self, nome, forca, pv):
        self._nome = nome
        self._for = forca
        self._pv_max = pv
        self._pv = self._pv_max

    def __repr__(self):
        return f'''Nome: {self._nome}
Pv: {self._pv}/{self._pv_max}
Força: {self._for}'''

    @property
    def pv(self):
        return self._pv

    @property
    def força(self):
        return self._pv

    def d_pv(self, n):
        self._pv += n

    @staticmethod
    def roll(die=2, bonus=0):
        res = DiceBag.roll(die, 6, bonus)
        return res


if __name__ == '__main__':
    char = Personagem('R')
    # char.roll()
    # print(sum(char.roll()))
    # print(char, '\n')
    # print('Ataque especial 1:')
    # print(Rules._Vantagens.ataque_especial(char, 1))
    print(char, '\n')
    #char._add_vantagem()
    #print(char, '\n')
    # print(char.select_vantagem(0))
    # print(char, '\n')
    #print(Combate.embate(char, char))
    # print('Ataque especial 2: \n', char.vantagens['ataque especial'.lower()](char, 1))
    # print(char, '\n')
    # print('Ataque especial 3: \n', Rules.vantagens['ataque especial'.lower()](char, 1))
    # print(char, '\n')
