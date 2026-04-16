#!/usr/bin/env python3

def create_archive(filename: str) -> None:
    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    f = open(filename, 'w')
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    i = 0
    for entry in entries:
        i += 1
        format_entry = f"[ENTRY {i:03d}] {entry}"
        f.write(format_entry + "\n")
        print(format_entry)
    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive("new_discovery.txt")
