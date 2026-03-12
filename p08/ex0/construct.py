

import sys
import os
import site

def get_virtual_env_info() -> dict:
    venv_path = os.environ.get('VIRTUAL_ENV')

    is_venv = (
        venv_path is not None or
        sys.prefix != sys.base_prefix or
        hasattr(sys, 'real_prefix')
    )

    venv_name = None
    if venv_path:
        venv_name = os.path.basename(venv_path)
    elif sys.prefix != sys.base_prefix:
        venv_name = os.path.basename(sys.prefix)

    return {
        "is_virtual_env": is_venv,
        "venv_path": venv_path or (sys.prefix if is_venv else None),
        "venv_name": venv_name,
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "base_prefix": sys.base_prefix,
        "prefix": sys.prefix
    }

def get_package_paths() -> list:
    return site.getsitepackages()

def display_matrix_status() -> None:
    info = get_virtual_env_info()

    print()

    if info["is_virtual_env"]:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {info['python_executable']}")
        print(f"Virtual Environment: {info['venv_name']}")
        print(f"Environment Path: {info['venv_path']}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        for path in get_package_paths():
            if "site-packages" in path:
                print(f"  {path}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {info['python_executable']}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("  python -m venv matrix_env")
        print("  source matrix_env/bin/activate  # On Unix")
        print("  matrix_env\\Scripts\\activate     # On Windows")
        print()
        print("Then run this program again.")

    print()

def show_environment_comparison() -> None:
    info = get_virtual_env_info()

    print("=" * 50)
    print("ENVIRONMENT COMPARISON")
    print("=" * 50)
    print(f"Base Python prefix: {info['base_prefix']}")
    print(f"Current prefix:     {info['prefix']}")
    print()

    if info["is_virtual_env"]:
        print("Global packages location:")
        print(f"  {info['base_prefix']}/lib/python{info['python_version'][:4]}/site-packages")
        print()
        print("Virtual env packages location:")
        for path in get_package_paths():
            if "site-packages" in path:
                print(f"  {path}")
    else:
        print("Current packages location (GLOBAL):")
        for path in get_package_paths():
            print(f"  {path}")

    print()

def main() -> None:
    display_matrix_status()
    show_environment_comparison()

if __name__ == "__main__":
    main()
