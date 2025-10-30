#!/usr/bin/env python3
"""
entropy_calc.py
Calculate Shannon entropy of a file (whole file or per chunk).

Usage:
    python3 entropy_calc.py <file_path> [chunk_size]

Example:
    python3 entropy_calc.py unpacked_malware.bin
    python3 entropy_calc.py unpacked_malware.bin 4096
"""

import sys
import math
from collections import Counter

def shannon_entropy(data: bytes) -> float:
    """Compute Shannon entropy (bits per byte)."""
    if not data:
        return 0.0
    freq = Counter(data)
    n = len(data)
    return -sum((count/n) * math.log2(count/n) for count in freq.values())

def analyze_file(path: str, chunk_size: int = None):
    """Calculate and print file entropy (optionally per chunk)."""
    with open(path, "rb") as f:
        data = f.read()

    if not chunk_size:
        entropy = shannon_entropy(data)
        print(f"\n[+] File: {path}")
        print(f"[+] Entropy: {entropy:.6f} bits/byte\n")
    else:
        print(f"\n[+] File: {path}")
        print(f"[+] Chunk size: {chunk_size} bytes\n")
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            entropy = shannon_entropy(chunk)
            print(f"Offset 0x{i:08X} - 0x{i + len(chunk) - 1:08X} | Entropy: {entropy:.6f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 entropy_calc.py <file_path> [chunk_size]")
        sys.exit(1)

    file_path = sys.argv[1]
    chunk_size = int(sys.argv[2]) if len(sys.argv) > 2 else None

    analyze_file(file_path, chunk_size)
