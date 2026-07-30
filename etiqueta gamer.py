'''
Módulo para gerenciamento e exibição estilizada de perfis de gamers.
Este módulo define a classe Gamer e utiliza a biblioteca Rich para
gerar fichas visuais e formatadas no terminal.
'''

#DECLARAÇÃO DA CLASSE
from rich import print
from rich.panel import Panel


class Gamer():
    """Representa um jogador de videogames e seus jogos favoritos.

        Atributos:
            nome (str): O nome real do jogador.
            apelido (str): O nickname ou apelido do jogador.
            jogos (list[str]): Lista com os nomes dos jogos favoritos.
    """

    def __init__(self, nome, nick):                 #Método Construtor
        '''Inicializa uma nova instância do jogador.

                Args:
                    nome (str): O nome real do jogador.
                    nick (str): O nickname ou apelido do jogador no jogo.
        '''

        #Atributos
        self.nome = nome
        self.apelido = nick
        self.jogos = []


        #Métodos
    def __str__(self):
        #Retorna uma representação em texto simples do objeto Gamer.
        return f'O gamer {self.nome} tem o apelido {self.apelido}'


    def add_favoritos(self,jogo):
        '''Adiciona um jogo à lista de favoritos do jogador e a ordena em ordem alfabética.

                Args:
                    jogo (str): Nome do jogo a ser adicionado.
        '''
        self.jogos.append(jogo)
        self.jogos.sort()



    def ficha(self):
        '''Imprime no terminal um painel formatado (Rich Panel) contendo a ficha do jogador
           e sua lista de jogos favoritos com ícones e cores.
        '''
        conteudo = f'Nome real: [white on blue]{self.nome}[/]\n'
        conteudo = conteudo + f'Jogos favoritos:\n'
        for num, game in enumerate(self.jogos):
            conteudo = conteudo + f'\n:video_game: [blue] {game} [/]'
        ficha = Panel(conteudo,title=f'Jogador(a) <{self.apelido}>',width=45)
        print(ficha)





# EXECUÇÃO / TESTES
#DECLARAÇÃO DOS OBJETOS
# Criando o primeiro jogador
g1 = Gamer('Fabrício da Silva', 'detonador2025')
g1.add_favoritos('Mario Bros')
g1.add_favoritos('FIFA 26')
g1.add_favoritos('God of War')
g1.add_favoritos('Sonic')
g1.ficha()
# Criando a segunda jogadora
g2 = Gamer('Olívia Souza','peach_raivosa')
g2.add_favoritos('Fortnite')
g2.add_favoritos('PES 2024')
g2.ficha()
