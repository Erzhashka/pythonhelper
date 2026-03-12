#!/usr/bin/env python3


def recover_ancient_text(filename: str = "ancient_fragment.txt") -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename, 'r', encoding='utf-8')
        print("Connection established...")
        print()
        print("RECOVERED DATA:")

        contents = vault.read()
        print(contents)

        vault.close()

        print()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_text()
