# Entropy Calculator
A lightweight Python utility for calculating Shannon entropy of binary files, useful for identifying packed, encrypted, or compressed regions during malware analysis.
## Features

- Calculate total file entropy (0–8 bits/byte)

- Optional chunk-based analysis to locate high-entropy sections

## Why Entropy Matters
Entropy reveals how random or structured data is.  
High entropy often points to compression or encryption, a common sign of packed malware.

| Entropy Range | Meaning | Typical Data Type |
|----------------|----------|------------------|
| 0 – 4 | Low randomness | Text, code |
| 4 – 6 | Moderate | Normal binaries |
| 6 – 7.5 | High | Compressed or obfuscated |
| 7.5 – 8 | Very high | Encrypted or packed |

## Example
Run the script on any binary file:

```bash
python3 entropy_calc.py sample.bin
```

Output: 
```
[+] File: x86_64
[+] Entropy: 6.488449 bits/byte
```

<img width="465" height="87" alt="image" src="https://github.com/user-attachments/assets/9bcd9682-630c-454d-a8f0-e8343e645e41" />

## Chunk Based Entropy
Chunk-based mode divides the file into smaller blocks (e.g., 4 KB each) and calculates entropy for each.
This is useful for spotting packed or encrypted regions inside otherwise normal code.

```
python3 entropy_calc.py sample.bin 4096
```
Output

```
[+] File: sample.bin
[+] Chunk size: 4096 bytes

Offset 0x00000000 - 0x00000FFF | Entropy: 2.945621
Offset 0x00001000 - 0x00001FFF | Entropy: 7.864319
Offset 0x00002000 - 0x00002FFF | Entropy: 7.923504
```
<img width="402" height="675" alt="image" src="https://github.com/user-attachments/assets/2ea663cd-50a0-4f4f-b371-f19397e4a945" />






