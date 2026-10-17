
from compression import lzw_compress, initial_dictionary
from display import display_dictionary, display_replacement


def main():
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


if __name__ == "__main__":
    main()