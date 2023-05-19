import random
import os

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')

def jogo():
    palavras = ["abacaxi", "pera", "maça"]
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra]
    
    chances = 6
    letras_erradas = []

    while chances > 0:
        limpa_tela()
        print("---------Jogo da FORCA-----------\n\n\n")
        print("Adivinhe a palavra abaixo:\n\n")
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[i] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if '_' not in letras_descobertas:
            print("\n\nVocê ganhou! A palavra era:", palavra)
            break
        if chances == 0:
            print("Você perdeu... A palavra era:", palavra)

if __name__ == "__main__":
    jogo()
