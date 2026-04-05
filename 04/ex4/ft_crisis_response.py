#!/usr/bin/env python3

def crisis_handler(filename: str) -> None:
    try:
        with open(filename) as vault:
            vault.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unexpected error {e}")
        print("STATUS: Crisis handled, system stable\n")
    else:
        print(
            "SUCCESS: Archive recovered- ``Knowledge preserved for humanity''"
        )
        print("STATUS: Normal operations resumed\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archive.txt")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    crisis_handler("classified_vault.txt")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")
