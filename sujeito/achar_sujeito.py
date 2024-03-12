# https://medium.com/turing-talks/pos-tagging-da-teoria-%C3%A0-implementa%C3%A7%C3%A3o-eafa59c9d115

from funcoes_processamento import dividir_texto_em_palavras
import os

CURRENT_DATASET = f"{os.path.dirname(__file__)}/datasets/dict_validation.csv"  # train, test, validation


def achar_sujeito(frase: str):
    tokens = dividir_texto_em_palavras(frase)

    if not os.path.exists(CURRENT_DATASET):
        print(
            f"O arquivo {CURRENT_DATASET} não foi encontrado. Rode o script sujeito/mac_morpho_to_dict.py para criar o arquivo."
        )

        os._exit(1)

    with open(CURRENT_DATASET, "r") as f:
        lines = f.readlines()

        found_words = []

        for token in tokens:
            for line in lines:
                word, pos_tag = line.split("|")

                if token.lower() == word:
                    found_words.append((word, pos_tag.strip()))

    print(f"Palavras encontradas: {found_words}")
