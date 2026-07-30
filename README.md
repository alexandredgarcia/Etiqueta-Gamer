# 🎮 Etiqueta Gamer 

Um script Python orientado a objetos que gerencia e exibe cartões/fichas de perfil de jogadores no terminal, com formatação rica, cores e ícones utilizando a biblioteca **[Rich](https://github.com/Textualize/rich)**.

---

## 🔍 Visão Geral

O projeto foi desenvolvido para demonstrar conceitos fundamentais do Python de forma prática e visualmente atraente:
- **Programação Orientada a Objetos (POO)**: Encapsulamento de atributos (nome, apelido, jogos) e métodos.
- **Interface de Linha de Comando Estilizada**: Uso do Rich Panel para transformar textos simples em painéis organizados no terminal.
- **Manipulação de Listas**: Inserção e ordenação automática alfabética dos jogos favoritos.

---

## ✨ Recursos

- 👤 **Cadastro de Jogadores**: Armazena o nome real e o nickname do jogador.
- 🎮 **Gerenciamento de Jogos Favoritos**: Permite adicionar jogos e os mantém ordenados alfabeticamente.
- 🎨 **Ficha Visual (Rich Panel)**: Exibe a ficha do jogador com bordas, cores personalizadas e ícones de videogame (🎮).

---

## 📐 Estrutura da Classe
```text
Atributo / Método      Tipo               Descrição
nome                  Atributo (str)      Nome real do jogador.
apelido               Atributo (str)      Nickname do jogador.
jogos                 Atributo (list)     Lista de jogos favoritos.
add_favoritos(jogo)   Método              Adiciona um jogo à lista e ordena em ordem alfabética.
ficha()               Método              Imprime o painel estilizado no terminal com as informações do perfil.
```
---

## 💻 Como Usar

from gamer import Gamer

# Criando uma instância do jogador
jogador = Gamer('Fabrício da Silva', 'detonador2025')

# Adicionando jogos favoritos
jogador.add_favoritos('Mario Bros')
jogador.add_favoritos('God of War')

# Exibindo a ficha formatada no terminal
jogador.ficha()

---

## 🖼️ Exemplo de Saída
```text
┌────────────── Jogador(a) <detonador2025> ──────────────┐
│ Nome real: Fabrício da Silva                           │
│ Jogos favoritos:                                       │
│                                                        │
│ 🎮 FIFA 26                                             │
│ 🎮 God of War                                          │
│ 🎮 Mario Bros                                          │
│ 🎮 Sonic                                               │
└────────────────────────────────────────────────────────┘
```
---

👤 Autor: Desenvolvido por Alexandre Dias Garcia

Aspirante em Desenvolvimento Python

🧑‍💻 Alexandre Dias Garcia 🔗 https://www.linkedin.com/in/alexandred-garcia

📧 alexandredgarcia23@gmail.com
