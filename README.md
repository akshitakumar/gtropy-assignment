#  Word Dictionary Search in Python

This project implements a word dictionary search tool in Python. It loads words from a `list.txt` file and allows users to search for exact matches. If a word isn't found, it suggests the closest matches using approximate string matching.

---

##  Features

- Efficient word lookup using Python `set`
- Suggests close matches for misspelled words using `difflib.get_close_matches`
- Case-insensitive and whitespace-trimmed input handling
- Handles corner cases like empty input or missing file
- Clean, modular, and readable code

---

## Files

| File         | Description                               |
|--------------|-------------------------------------------|
| `main.py`    | Main Python script for dictionary search  |
| `list.txt`   | Word list file with one word per line     |

---
