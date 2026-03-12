#!/usr/bin/env python3
"""
Exercise 3: Vault Security

Mission: Implement failsafe storage procedures using context managers.
This exercise teaches the use of the 'with' statement (context manager)
to ensure proper file handling and automatic resource cleanup.

Authorized functions: open(), read(), write(), print()
Required: Must use 'with' statement for all file operations
"""


def secure_vault_operations() -> None:
    """
    Perform secure file operations using the 'with' statement.

    The 'with' statement ensures:
    1. The file is properly opened
    2. Operations execute within a protected context
    3. The file is automatically closed, even if errors occur

    This implements the RAII principle (Resource Acquisition Is Initialization)
    which guarantees proper resource cleanup.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    # Secure extraction using context manager
    print("SECURE EXTRACTION:")
    with open("classified_data.txt", 'r', encoding='utf-8') as vault:
        # Read and display classified data
        contents = vault.read()
        for line in contents.strip().split('\n'):
            print(line)
    # Vault automatically sealed when exiting 'with' block

    print()

    # Secure preservation using context manager
    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", 'r', encoding='utf-8') as vault:
        # Read security protocols
        protocols = vault.read()
        print(protocols.strip())
    # Vault automatically sealed when exiting 'with' block

    print()
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    secure_vault_operations()
