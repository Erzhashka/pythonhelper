#!/usr/bin/env python3
"""
Exercise 2: Stream Management

Mission: Master the three sacred data channels of the Archives.
This exercise teaches how to work with standard input, standard output,
and standard error streams using sys module.

Authorized: sys, sys.stdin, sys.stdout, sys.stderr, input(), print()
"""

import sys


def stream_management() -> None:
    """
    Demonstrate proper usage of the three data channels:
    - stdin: Input stream for receiving data
    - stdout: Standard output for normal messages
    - stderr: Error stream for alerts and diagnostics
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    # Input Stream - collecting archivist identification
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    # Standard Output Channel - normal data transmission
    sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: "
                     f"{status_report}\n")

    # Alert Channel - system diagnostics and warnings
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")

    # Standard Output - completion message
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
