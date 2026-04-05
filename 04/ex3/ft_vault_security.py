#!usr/bin/env python3

def secure_vault() -> None:
    print("\nSECURE EXTRACTION:")
    try:
        with open("vault_data.txt") as f:
            for line in f:
                print(f"[CLASSIFIED] {line.strip()}")
    except FileNotFoundError as e:
        print(f"Error: {e} I need sys to out to stderr!!!!")

    print("\nSECURE PRESERVATION:")
    try:
        with open("vault_data.txt", 'w') as f:
            f.write("New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
    except PermissionError as e:
        print(f"Error: {e} I need sys to out to stderr!!!!")
    finally:
        print("Vault automatically sealed upon completion")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    secure_vault()

    print("\nAll vault operations completed with maximum security.")
