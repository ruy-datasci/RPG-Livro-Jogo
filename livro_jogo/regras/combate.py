from dice.livro_jogo.core import Seletor


class Combate:
    def __init__(self, personagem, oponentes, n_turn=1):
        self.personagem = personagem
        self.oponente = oponentes
        self.n_turn = n_turn
        self.vantagens = set()
        self.opcoes = {'Atacar': None}
        if personagem.vantagens.keys():
            self.opcoes['Vantagens'] = self.personagem.vantagens

    def turno(self, vantagem=None):
        if vantagem is None:
            oponente_roll , personagem_roll = self.oponente.roll(), self.personagem.roll()
        else:
            print(vantagem)
            oponente_roll , personagem_roll = vantagem.executar(self)
            self.vantagens.add(vantagem)
        res_oponente, res_personagem = self.oponente.força+sum(oponente_roll), self.personagem.força+sum(personagem_roll)
        res = res_personagem-res_oponente
        print(f'Resultado do personagem: {res_personagem} {personagem_roll}\nResultado do oponente: {res_oponente} {oponente_roll}')
        print(f'{abs(res)} de dano no {"personagem" if res<0 else "oponente"}')
        if res < 0: self.personagem.d_pv(-abs(res))
        elif res > 0: self.oponente.d_pv(-abs(res))
        self.n_turn += 1
        return self

    def executar(self):
        while (self.personagem.pv > 0) and (self.oponente.pv > 0):
            print(self.personagem)
            print('Turno: ',self.n_turn)
            vantagem = Seletor.selecionar(self.opcoes)
            if isinstance(vantagem, dict):
                vantagem.update({'Sair':None})
                self.turno(Seletor.selecionar(vantagem))
            else:
                self.turno(vantagem)
        print(self.personagem)
        if (self.personagem.pv <= 0):
            print('Você perdeu')
        if (self.oponente.pv <= 0):
            print('O inimigo perdeu')
        return self


if __name__ == '__main__':
    from dice.book_sheet import Personagem, Criatura
    from dice.livro_jogo.regras.regras import Regras
    char = Personagem('R', Regras.races['Humano'], Regras.classes['Guerreiro'])
    opo = Criatura('A', 7, 15)
    print(opo)
    comb = Combate(char, opo)
    comb.executar()
