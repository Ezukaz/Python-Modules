#!/usr/bin/env python3


def create_archive(filename: str) -> None:
    """Create new archive with preservation data"""
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
    for i, entry in enumerate(entries):
        f.write(entry + "\n")
        print(f"[ENTRY {i + 1:03d}] {entry}")
    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive("new_discovery.txt")
