#!/usr/bin/env python3

def recover_data(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print(f"Accessing Storage Vault: {filename}")
    try:
        f = open(filename, 'r')
        content = f.read()
        f.close()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        lines = content.split("\n")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
