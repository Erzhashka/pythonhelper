#!/usr/bin/env python3
"""
Exercise 1: Archive Creation

Mission: Establish new data preservation protocols by creating archive entries.
This exercise teaches basic file writing operations using open(), write(),
close(), and print().

Authorized functions: open(), write(), close(), print()
"""


def create_archive(filename: str = "new_discovery.txt") -> None:
    """
    Create a new archive and inscribe preservation data.

    Args:
        filename: The name of the file to create for the new archive.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")

    # Open the storage unit in write mode (creates new or overwrites)
    vault = open(filename, 'w', encoding='utf-8')
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")

    # Define the entries to inscribe
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    # Write each entry to the archive
    for entry in entries:
        vault.write(entry + "\n")
        print(entry)

    # Close the storage unit
    vault.close()

    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive()
