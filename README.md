# LZW Compression

A Python implementation of the **Lempel-Ziv-Welch (LZW)** lossless compression algorithm. It compresses a string into a sequence of dictionary codes, decompresses it back, and shows the dictionary built along the way.

## Features

- Compresses strings over the alphabet `{a, b, c}` into LZW codes
- Decompresses a sequence of codes back into the original string
- Displays the generated dictionary as a table (code, substring, origin)
- Maps every output code to its dictionary substring
- Validates user input (empty input, unsupported characters, invalid codes)
- Modular design: compression, decompression and display are kept separate

## Project Structure

```
lzw-compression/
├── compression.py     # LZW compression logic
├── decompression.py   # LZW decompression logic
├── display.py         # Output formatting helpers
├── main.py            # Command-line entry point
└── README.md
```

| File | Description |
|------|-------------|
| `compression.py` | `initial_dictionary()` builds the starting dictionary. `lzw_compress(text)` returns the output codes and the final dictionary. |
| `decompression.py` | `lzw_decompress(codes)` rebuilds the original string and the final dictionary from a list of codes. |
| `display.py` | `display_dictionary()` prints the dictionary table. `display_replacement()` replaces each code with its substring. |
| `main.py` | Menu to choose compression or decompression, validates the input and prints the results. |

## Getting Started

### Prerequisites

- Python 3.8 or later
- No external dependencies

### Installation

```bash
git clone <repository-url>
cd lzw-compression
```

### Usage

```bash
python main.py
```

Choose an option from the menu:

1. **Compression**: enter a string made of `a`, `b` and `c`.
2. **Decompression**: enter the codes separated by spaces, for example `0 1 3 3 2 6`.

Invalid input is rejected with an error message: an empty entry, a character outside `{a, b, c}`, a code that is not a number, or a code sequence that cannot come from a valid compression (for example `0 9`).

## Examples

### Compression

Input: `abababcabc`

```
Chaîne d'entrée : abababcabc
Codes de sortie : [0, 1, 3, 3, 2, 6]

=== Dictionnaire ===
Code  | Sous-chaîne    | Origine
----------------------------------------
0     | a              | initial
1     | b              | initial
2     | c              | initial
3     | ab             | ajouté
4     | ba             | ajouté
5     | aba            | ajouté
6     | abc            | ajouté
7     | ca             | ajouté

=== Remplacement des codes par les sous-chaînes ===
0  ->  a
1  ->  b
3  ->  ab
3  ->  ab
2  ->  c
6  ->  abc

Codes        : 0 1 3 3 2 6
Sous-chaînes : a | b | ab | ab | c | abc
```

### Decompression

Input: `0 1 3 3 2 6`

```
Codes d'entrée      : [0, 1, 3, 3, 2, 6]
Chaîne décompressée : abababcabc
```

The dictionary and the code-to-substring table are then displayed in the same format as above, and the dictionary is identical to the one built during compression.

### Decompression: special case

A code can refer to a dictionary entry that has not been created yet. Input: `0 3`

```
Codes d'entrée      : [0, 3]
Chaîne décompressée : aaa

=== Dictionnaire ===
Code  | Sous-chaîne    | Origine
----------------------------------------
0     | a              | initial
1     | b              | initial
2     | c              | initial
3     | aa             | ajouté

=== Remplacement des codes par les sous-chaînes ===
0  ->  a
3  ->  aa

Codes        : 0 3
Sous-chaînes : a | aa
```

Code `3` is not in the dictionary when it is read. It is rebuilt as the previous substring (`a`) plus its own first character, which gives `aa`.

## Use as a Library

The functions can also be imported and used directly:

```python
from compression import lzw_compress
from decompression import lzw_decompress

codes, dictionary = lzw_compress("abababcabc")
print(codes)                        # [0, 1, 3, 3, 2, 6]

text, dictionary = lzw_decompress(codes)
print(text)                         # abababcabc
```

Decompressing the output of the compressor always returns the original string, and both directions produce the same dictionary.

## How It Works

**Compression**

- The dictionary starts with the single symbols `a = 0`, `b = 1`, `c = 2`.
- The input is read character by character, always extending the longest substring already in the dictionary.
- When a substring is not found, the code of its known prefix is output and the new substring is added to the dictionary.

**Decompression**

- The same initial dictionary is rebuilt, then the first code is decoded directly.
- Each following code is decoded, and the previous substring extended with the first character of the current one is added to the dictionary.
- A code can refer to an entry that does not exist yet. This happens when the compressor used an entry the moment it created it, and it is resolved as `previous + first character of previous`. For example, the codes `0 3` decode to `aaa`.

