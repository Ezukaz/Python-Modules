#!/usr/bin/env python3


def recover_data(filename: str) -> None:
    """Recover ancient data from storage vault"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print(f"Accessing Storage Vault: {filename}")
    try:
        f = open(filename, 'r')
        content = f.read()
        f.close()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        lines = content.strip().split("\n")
        for i, line in enumerate(lines):
            print(f"[FRAGMENT {i + 1:03d}] {line}")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    else:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
