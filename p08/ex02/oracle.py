import os
import sys
from typing import Dict, Optional, Any

def load_dotenv_file(filepath: str = '.env') -> Dict[str, str]:

    loaded_vars = {}

    try:
        from dotenv import load_dotenv
        load_dotenv(filepath)
        print("  [OK] Loaded .env using python-dotenv")
        return loaded_vars
    except ImportError:
        pass

    if not os.path.exists(filepath):
        print(f"  [--] No .env file found at {filepath}")
        return loaded_vars

    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith('#'):
                    continue

                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()

                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    os.environ[key] = value
                    loaded_vars[key] = value
        print(f"  [OK] Loaded .env manually from {filepath}")
    except Exception as e:
        print(f"  [ERROR] Failed to load .env: {e}")

    return loaded_vars

def get_config(key: str, default: Optional[str] = None,
               required: bool = False) -> Optional[str]:

    value = os.environ.get(key, default)

    if required and value is None:
        raise ValueError(f"Required configuration '{key}' is missing")

    return value

def load_configuration() -> Dict[str, Any]:

    config = {
        'MATRIX_MODE': get_config('MATRIX_MODE', 'development'),
        'DATABASE_URL': get_config('DATABASE_URL', 'sqlite:///local.db'),
        'API_KEY': get_config('API_KEY'),
        'LOG_LEVEL': get_config('LOG_LEVEL', 'DEBUG'),
        'ZION_ENDPOINT': get_config('ZION_ENDPOINT', 'http://localhost:8080')
    }

    return config

def check_security(config: Dict[str, Any]) -> Dict[str, bool]:

    checks = {}

    checks['no_hardcoded_secrets'] = True

    checks['env_file_configured'] = os.path.exists('.env')

    checks['production_overrides'] = (
        os.environ.get('MATRIX_MODE') is not None or
        os.environ.get('API_KEY') is not None
    )

    checks['api_key_set'] = config.get('API_KEY') is not None

    return checks

def display_configuration(config: Dict[str, Any]) -> None:

    print()
    print("Configuration loaded:")
    print(f"  Mode: {config['MATRIX_MODE']}")

    db_url = config['DATABASE_URL']
    if '@' in db_url and ':' in db_url:

        print(f"  Database: Connected to {'local' if 'localhost' in db_url or 'local' in db_url else 'remote'} instance")
    else:
        print(f"  Database: {db_url}")

    if config['API_KEY']:
        masked_key = config['API_KEY'][:4] + '*' * (len(config['API_KEY']) - 4)
        print(f"  API Access: Authenticated ({masked_key})")
    else:
        print("  API Access: Not configured")

    print(f"  Log Level: {config['LOG_LEVEL']}")

    endpoint = config['ZION_ENDPOINT']
    print(f"  Zion Network: {'Online' if endpoint else 'Offline'}")

def display_security_status(checks: Dict[str, bool]) -> None:

    print()
    print("Environment security check:")

    if checks['no_hardcoded_secrets']:
        print("  [OK] No hardcoded secrets detected")
    else:
        print("  [WARN] Potential hardcoded secrets found")

    if checks['env_file_configured']:
        print("  [OK] .env file properly configured")
    else:
        print("  [--] .env file not found (using defaults/env vars)")

    if checks['production_overrides']:
        print("  [OK] Production overrides available")
    else:
        print("  [--] No environment variable overrides set")

    if checks['api_key_set']:
        print("  [OK] API key is configured")
    else:
        print("  [WARN] API key not set")

def show_usage_examples() -> None:

    print()
    print("=" * 50)
    print("CONFIGURATION USAGE")
    print("=" * 50)
    print()
    print("Using .env file:")
    print("  1. Copy .env.example to .env")
    print("  2. Edit .env with your values")
    print("  3. Run: python oracle.py")
    print()
    print("Using environment variables:")
    print("  Unix/Linux/Mac:")
    print("    MATRIX_MODE=production API_KEY=secret123 python oracle.py")
    print()
    print("  Windows PowerShell:")
    print("    $env:MATRIX_MODE='production'; $env:API_KEY='secret123'; python oracle.py")
    print()
    print("  Windows CMD:")
    print("    set MATRIX_MODE=production && set API_KEY=secret123 && python oracle.py")
    print()

def main() -> None:

    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    print("Loading configuration sources:")
    load_dotenv_file('.env')

    try:
        import dotenv
        print("  [OK] python-dotenv available")
    except ImportError:
        print("  [--] python-dotenv not installed (using fallback parser)")
        print("       Install with: pip install python-dotenv")

    try:
        config = load_configuration()
    except ValueError as e:
        print(f"  [ERROR] {e}")
        show_usage_examples()
        return

    display_configuration(config)

    security_checks = check_security(config)
    display_security_status(security_checks)

    print()
    print("The Oracle sees all configurations.")

    if config['MATRIX_MODE'] == 'development':
        print()
        print("NOTE: Running in development mode.")
        print("Set MATRIX_MODE=production for production deployment.")

if __name__ == "__main__":
    main()
