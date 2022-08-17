from dice.livro_jogo.regras.core import Vantagens, Raça, Classe

#Vantagens


class AtaqueADistancia(metaclass=Vantagens):
    _nome = 'ataque a distancia'

    @classmethod
    def executar(self, combate):
        if combate.n_turn == 1 and combate.personagem.pm >= 1:
            roll = combate.personagem.roll(1)
            combate.oponente.d_pv(-sum(roll))
            combate.personagem.d_pm(-1)
        elif combate.n_turn != 1:
            print(f'{self._nome} só pode ser usado na primeira rodada')
        else:
            print('Você não possui pm suficiente para esta opção')
        return combate.oponente.roll(), combate.personagem.roll()

    @classmethod
    def reset(self): pass


class AtaqueEspecial(metaclass=Vantagens):
    _nome = 'ataque especial'

    @classmethod
    def executar(self, combate):
        if combate.personagem.pm >= 1:
            combate.personagem.d_pm(-1)
            return combate.oponente.roll(), combate.personagem.roll(3)
        else:
            print('Você não possui pm suficiente para esta opção')
            return combate.oponente.roll(), combate.personagem.roll()

    @classmethod
    def reset(self): pass


class Regras:
    races = {
        'Humano': {
            'Força': 7,
            'Habilidade': 7,
            'pv': 10,
            'pm': 10,
        },
        'Anão': {
            'Força': 8,
            'Habilidade': 6,
            'pv': 15,
            'pm': 5,
        },
    }
    races = {
        chave: Raça(chave,
                    valor['Força'],
                    valor['Habilidade'],
                    valor['pv'],
                    valor['pm'],
                    ) for chave, valor in races.items()}
    classes = {
        'Clérigo': {
            'Força': 0,
            'Habilidade': 0,
            'pv': 0,
            'pm': 5,
            'Vantagens': 'Magias divinas',
        },
        'Guerreiro': {
            'Força': 1,
            'Habilidade': 0,
            'pv': 5,
            'pm': 0,
            'Vantagens': '',
        },
    }
    classes = {
        chave: Classe(chave,
                      valor['Força'],
                      valor['Habilidade'],
                      valor['pv'],
                      valor['pm'],
                      valor['Vantagens']
                      ) for chave, valor in classes.items()}
    vantagens = [
        AtaqueADistancia,
        AtaqueEspecial
    ]
    vantagens = {str(vantagem): vantagem for vantagem in vantagens}
    vantagens['Sair'] = False
    opcoes_pontos = {
        'Força +1': lambda self: self._d_pontos(-1)._d_forca(1) if self._pontos > 0 else self,
        'Habilidade +1': lambda self: self._d_pontos(-1)._d_hab(1) if self._pontos > 0 else self,
        'pv +5': lambda self: self._d_pontos(-1)._d_pv_max(5) if self._pontos > 0 else self,
        'pm +5': lambda self: self._d_pontos(-1)._d_pm_max(5) if self._pontos > 0 else self,
        'Vantagens': lambda self: self._d_pontos(-1)._add_vantagem() if self._pontos > 0 else self,
    }


if __name__ == '__main__':
    from dice.book_sheet import Personagem, Criatura
    char = Personagem('R', Regras.races['Humano'], Regras.classes['Guerreiro'])
    opo = Criatura('A', 7, 15)
    print(char)
    print(opo)
