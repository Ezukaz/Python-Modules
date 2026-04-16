#!usr/bin/env python3

def secure_vault() -> None:
    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt") as f:
            for line in f:
                print(line)
        print("\nSECURE PRESERVATION:")
        with open("classified_data.txt", 'w') as f:
            f.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("Vault automatically sealed upon completion")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    secure_vault()

    print("\nAll vault operations completed with maximum security.")
