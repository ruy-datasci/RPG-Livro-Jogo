class Seletor:
    @staticmethod
    def selecionar(mapa: dict, block: dict = {}):
        opcoes = {str(key): value for key, value in enumerate(mapa.keys()) if value not in block.keys()}
        for key, value in opcoes.items():
            print(key, ': ', value)
        n = input('Selecione a opção desejada: ')
        if n in opcoes.keys():
            return mapa[opcoes[n]]
        else:
            print('Erro: opção inválida')
            return Seletor.selecionar(mapa, block)
