import random
import os


class Jogo:
    chances = 8
    letras_erradas = []
    palavras = ["abacaxi", "pera", "maça"]
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for letra in palavra]
    boneco = [
        '''\n
+---+
|   |
    |
    |
    |
    |
=========''',
        '''\n
+---+
|   |
O   |
    |
    |
    |
=========''',
        '''\n
+---+
|   |
O   |
|   |
    |
    |
=========''',
        '''\n
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''',
        '''\n
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''',
        '''\n
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''',
        '''\n
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''',
        '''\n
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========='''
    ]

    def limpa_tela(self):
        if os.name == 'nt':
            _ = os.system('cls')


class InicializarJogo(Jogo):
    def tentativa_usuario(self):
        tentativa = input("\nDigite uma letra: ").lower()
        if tentativa in self.palavra:
            for i, letra in enumerate(self.palavra):
                if tentativa == letra:
                    self.letras_descobertas[i] = letra
        else:
            Jogo.chances -= 1
            self.letras_erradas.append(tentativa)

    def ganhou(self):
        print("\n\nVocê ganhou! A palavra era:", self.palavra)

    def perdeu(self):
        print("Você perdeu... A palavra era:", self.palavra)

    def update_tela(self):
        print("---------Jogo da FORCA-----------\n\n\n")
        print(self.boneco[len(self.letras_erradas)])
        print("Adivinhe a palavra abaixo:\n\n")
        print(" ".join(self.letras_descobertas))
        print("\nChances restantes:", Jogo.chances)
        print("Letras erradas:", " ".join(self.letras_erradas))


def main():
    jogar = Jogo()
    atualizar = InicializarJogo()

    while Jogo.chances > 0:
        jogar.limpa_tela()
        atualizar.update_tela()
        atualizar.tentativa_usuario()
        if '_' not in jogar.letras_descobertas:
            atualizar.ganhou()
            break
        if Jogo.chances == 0:
            atualizar.perdeu()


if __name__ == "__main__":
    main()