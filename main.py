from lista import banco_de_musicas
from random import randint
import pandas as pd

print("Bem-vindo(a) ao Spotify Music!")

flag = 0
while flag == 0:
    opc = int(input("Qual música você gostaria de ouvir? Selecione um número de 0 a 99: \n"))
    musica_selecionada = banco_de_musicas[opc]["nome"]
    artista_selecionado = banco_de_musicas[opc]["artista"]

    print(f"Agora ouvindo: {musica_selecionada} de {artista_selecionado}")
    while True:
        menu = int(input("""
        1 - Próxima faixa
        2 - Encerrar aplicativo
        3 - Modo aleatório
        4 - Modo One Way \n"""))
        if menu == 1:
            opc += 1
            if opc >= len(banco_de_musicas):
                opc = 0
            musica_selecionada = banco_de_musicas[opc]["nome"]
            artista_selecionado = banco_de_musicas[opc]["artista"]
            print(f"Agora ouvindo: {musica_selecionada} de {artista_selecionado}")
        elif menu == 2:
            print("Obrigado por utilizar Spotify Music")
            flag = 1
            break
        elif menu == 3:
            opc = randint(0,99)
            musica_selecionada = banco_de_musicas[opc]["nome"]
            artista_selecionado = banco_de_musicas[opc]["artista"]
            print(f"Agora ouvindo: {musica_selecionada} de {artista_selecionado}")
        elif menu == 4:
            if opc is not None:
                if "genero_atual" not in locals():
                    genero_atual = "subgênero"

                # Criar um DataFrame pandas
                df = pd.DataFrame(banco_de_musicas)

                # Selecionar a música que está tocando
                musica_tocando = df.loc[opc]

                if genero_atual == "subgênero":
                    # Selecionar músicas do mesmo subgênero e gênero da música que está tocando
                    musicas_mesmo_genero = df[(df["subgênero"] == musica_tocando["subgênero"]) & (df["gênero"] == musica_tocando["gênero"])]

                    # Exibir as músicas do mesmo subgênero e gênero
                    print("Músicas do mesmo subgênero e gênero:")
                    print(musicas_mesmo_genero)

                    genero_atual = "gênero"
                else:
                    # Selecionar músicas do mesmo gênero da música que está tocando
                    musicas_mesmo_genero = df[df["gênero"] == musica_tocando["gênero"]]

                    # Exibir as músicas do mesmo gênero
                    print("Músicas do mesmo gênero:")
                    print(musicas_mesmo_genero)

                    genero_atual = "subgênero"
            else:
                print("Por favor, selecione uma música antes de usar o Modo One Way.")
