#!/usr/bin/env python3
"""
Exercise 4: Crisis Response

Mission: Handle corrupted archives and access failures gracefully.
This exercise combines context managers ('with' statement) with
exception handling (try/except) for robust error management.

Authorized functions: open(), read(), write(), print()
Required: Must use both 'with' statement AND try/except blocks
Must handle: FileNotFoundError, PermissionError, and other exceptions
"""


def crisis_handler(filename: str) -> None:
    """
    Handle archive access with comprehensive error management.

    This function implements crisis response protocols:
    - FileNotFoundError: Archive not found in storage matrix
    - PermissionError: Security protocols deny access
    - Other exceptions: Unexpected system anomalies

    Args:
        filename: The name of the archive to access.
    """
    is_routine = filename == "standard_archive.txt"

    if is_routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, 'r', encoding='utf-8') as vault:
            content = vault.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {type(e).__name__}")
        print("STATUS: Crisis contained, investigating cause")

    print()


def crisis_response_system() -> None:
    """
    Run the complete crisis response system testing various scenarios.

    Tests include:
    1. Missing archive (FileNotFoundError)
    2. Restricted vault (PermissionError simulation)
    3. Standard archive recovery (successful operation)
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    # Test 1: Missing archive
    crisis_handler("lost_archive.txt")

    # Test 2: Classified vault (simulating access denial)
    # Note: True PermissionError requires OS-level restrictions
    crisis_handler("classified_vault.txt")

    # Test 3: Standard archive recovery
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response_system()
