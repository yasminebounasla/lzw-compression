# LZW Compression

A Python implementation of the **Lempel-Ziv-Welch (LZW)** lossless compression algorithm. It compresses a string into a sequence of dictionary codes and shows the dictionary built along the way.

## Features

- Compresses strings over the alphabet `{a, b, c}` into LZW codes
- Displays the generated dictionary as a table (code, substring, origin)
- Maps every output code back to its dictionary substring
- Validates user input (empty string, unsupported characters)
- Modular design: compression logic and display are kept separate

## Project Structure

```
lzw-compression/
├── compression.py   # LZW compression logic
├── display.py       # Output formatting helpers
├── main.py          # Command-line entry point
└── README.md
```

| File | Description |
|------|-------------|
| `compression.py` | `initial_dictionary()` builds the starting dictionary. `lzw_compress(text)` returns the output codes and the final dictionary. |
| `display.py` | `display_dictionary()` prints the dictionary table. `display_replacement()` replaces each code with its substring. |
| `main.py` | Reads and validates the input, then runs compression and prints the results. |

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

Enter a string made of `a`, `b` and `c` when prompted.

## Example

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

Joining the substrings `a`, `b`, `ab`, `ab`, `c`, `abc` gives back the original string.

## How It Works

- The dictionary starts with the single symbols `a = 0`, `b = 1`, `c = 2`.
- The input is read character by character, always extending the longest substring already in the dictionary.
- When a substring is not found, the code of its known prefix is output and the new substring is added to the dictionary.

