
# Print the dictionary as a table: code | substring | origin.
def display_dictionary(dictionary, initial_size=3):

    entries = sorted(dictionary.items(), key=lambda item: item[1]) # {"a": 0} --> [("a", 0)]

    print("\n=== Dictionnaire ===")
    print(f"{'Code':<6}| {'Sous-chaîne':<15}| Origine") # display header
    print("-" * 40)

    for substring, code in entries:                              # display each entry
        origin = "initial" if code < initial_size else "ajouté"  
        print(f"{code:<6}| {substring:<15}| {origin}")



# Print the replacement of codes with their corresponding substrings.
def display_replacement(codes, dictionary):
    
    # Reverse the dictionary: code -> substring
    reverse = {code: substring for substring, code in dictionary.items()}

    print("\n=== Remplacement des codes par les sous-chaînes ===")
    for code in codes:                                           
        print(f"{code}  ->  {reverse[code]}")

    substrings = [reverse[code] for code in codes]
    print("\nCodes        :", " ".join(str(c) for c in codes))
    print("Sous-chaînes :", " | ".join(substrings))