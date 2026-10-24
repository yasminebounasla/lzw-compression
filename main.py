"""Entry point: LZW compression and decompression."""

from compression import lzw_compress, initial_dictionary
from decompression import lzw_decompress
from display import display_dictionary, display_replacement


def run_compression():
    alphabet = list(initial_dictionary())   # ['a', 'b', 'c']

    text = input(f"Entrez une chaîne de l'alphabet {{{', '.join(alphabet)}}} : ").strip()

    # Validate the input
    if not text:
        print("Erreur : la chaîne est vide.")
        return
    if any(c not in alphabet for c in text):
        print(f"Erreur : seuls les caractères {alphabet} sont autorisés.")
        return

    codes, dictionary = lzw_compress(text)

    print("\nChaîne d'entrée :", text)
    print("Codes de sortie :", codes)

    display_dictionary(dictionary)
    display_replacement(codes, dictionary)


def run_decompression():
    raw = input("Entrez les codes séparés par des espaces (ex : 0 1 3 3 2 6) : ").strip()

    # Validate the input
    if not raw:
        print("Erreur : aucun code saisi.")
        return
    try:
        codes = [int(part) for part in raw.split()]
    except ValueError:
        print("Erreur : les codes doivent être des nombres entiers.")
        return

    try:
        text, dictionary = lzw_decompress(codes)
    except ValueError as error:
        print(f"Erreur : séquence de codes invalide ({error}).")
        return

    print("\nCodes d'entrée      :", codes)
    print("Chaîne décompressée :", text)

    display_dictionary(dictionary)
    display_replacement(codes, dictionary)


def main():
    print("1. Compression")
    print("2. Décompression")
    choice = input("Votre choix (1 ou 2) : ").strip()

    if choice == "1":
        run_compression()
    elif choice == "2":
        run_decompression()
    else:
        print("Erreur : choix invalide.")


if __name__ == "__main__":
    main()