import sys
import importlib.util
from typing import Dict, List, Tuple, Optional

def check_package(package_name: str) -> Tuple[bool, Optional[str]]:

    try:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            return False, None

        try:
            module = importlib.import_module(package_name)
            version = getattr(module, '__version__', 'unknown')
            return True, version
        except ImportError:
            return False, None
    except ModuleNotFoundError:
        return False, None

def check_dependencies() -> Dict[str, Tuple[bool, Optional[str]]]:

    required_packages = ['pandas', 'numpy', 'matplotlib']
    optional_packages = ['requests']

    results = {}

    print("Checking dependencies:")

    for package in required_packages:
        installed, version = check_package(package)
        results[package] = (installed, version)

        if installed:
            print(f"  [OK] {package} ({version}) - Ready")
        else:
            print(f"  [MISSING] {package} - Not installed")

    for package in optional_packages:
        installed, version = check_package(package)
        results[package] = (installed, version)

        if installed:
            print(f"  [OK] {package} ({version}) - Optional, available")
        else:
            print(f"  [--] {package} - Optional, not installed")

    return results

def show_installation_instructions() -> None:

    print()
    print("=" * 50)
    print("INSTALLATION INSTRUCTIONS")
    print("=" * 50)
    print()
    print("Using pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Using Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print()
    print("Manual installation:")
    print("  pip install pandas numpy matplotlib")
    print()

def show_pip_vs_poetry_comparison() -> None:

    print()
    print("=" * 50)
    print("PIP vs POETRY COMPARISON")
    print("=" * 50)
    print()
    print("PIP (requirements.txt):")
    print("  + Simple, widely supported")
    print("  + Easy to understand")
    print("  - No lock file by default")
    print("  - Manual dependency resolution")
    print()
    print("POETRY (pyproject.toml):")
    print("  + Automatic lock file (poetry.lock)")
    print("  + Dependency resolution")
    print("  + Virtual env management")
    print("  + Build and publish support")
    print("  - Learning curve")
    print()

def analyze_matrix_data() -> None:

    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"ERROR: Missing dependency - {e}")
        show_installation_instructions()
        return

    print()
    print("Analyzing Matrix data...")

    np.random.seed(42)
    n_points = 1000

    data = pd.DataFrame({
        'timestamp': pd.date_range('2199-01-01', periods=n_points, freq='h'),
        'signal_strength': np.random.randn(n_points).cumsum() + 100,
        'anomaly_score': np.random.exponential(scale=2, size=n_points),
        'node_activity': np.random.poisson(lam=50, size=n_points),
        'sentinel_proximity': np.abs(np.random.randn(n_points) * 20)
    })

    print(f"Processing {n_points} data points...")

    print()
    print("Data Summary:")
    print(f"  Signal Strength - Mean: {data['signal_strength'].mean():.2f}")
    print(f"  Anomaly Score - Max: {data['anomaly_score'].max():.2f}")
    print(f"  Node Activity - Total: {data['node_activity'].sum()}")
    print(f"  Sentinel Alerts: {(data['sentinel_proximity'] > 30).sum()}")

    print()
    print("Generating visualization...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Matrix Data Analysis', fontsize=14, fontweight='bold')

    axes[0, 0].plot(data['timestamp'], data['signal_strength'],
                    color='green', linewidth=0.5)
    axes[0, 0].set_title('Signal Strength Over Time')
    axes[0, 0].set_xlabel('Timestamp')
    axes[0, 0].set_ylabel('Strength')
    axes[0, 0].tick_params(axis='x', rotation=45)

    axes[0, 1].hist(data['anomaly_score'], bins=30, color='red', alpha=0.7)
    axes[0, 1].set_title('Anomaly Score Distribution')
    axes[0, 1].set_xlabel('Score')
    axes[0, 1].set_ylabel('Frequency')

    axes[1, 0].scatter(range(len(data)), data['node_activity'],
                       c='cyan', alpha=0.3, s=5)
    axes[1, 0].set_title('Node Activity Pattern')
    axes[1, 0].set_xlabel('Sample')
    axes[1, 0].set_ylabel('Activity')

    axes[1, 1].fill_between(range(len(data)), data['sentinel_proximity'],
                            color='purple', alpha=0.5)
    axes[1, 1].axhline(y=30, color='red', linestyle='--', label='Alert Threshold')
    axes[1, 1].set_title('Sentinel Proximity')
    axes[1, 1].set_xlabel('Sample')
    axes[1, 1].set_ylabel('Proximity')
    axes[1, 1].legend()

    plt.tight_layout()

    output_file = 'matrix_analysis.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")

def show_installed_versions() -> None:

    print()
    print("=" * 50)
    print("INSTALLED PACKAGE VERSIONS")
    print("=" * 50)

    packages = ['pandas', 'numpy', 'matplotlib', 'requests', 'pip']

    for package in packages:
        installed, version = check_package(package)
        if installed:
            print(f"  {package}: {version}")
        else:
            print(f"  {package}: not installed")

    print()

def main() -> None:

    print()
    print("LOADING STATUS: Loading programs...")
    print()

    deps = check_dependencies()

    required = ['pandas', 'numpy', 'matplotlib']
    missing = [pkg for pkg in required if not deps.get(pkg, (False,))[0]]

    if missing:
        print()
        print(f"WARNING: Missing required packages: {', '.join(missing)}")
        show_installation_instructions()
        show_pip_vs_poetry_comparison()
        return

    analyze_matrix_data()

    show_pip_vs_poetry_comparison()
    show_installed_versions()

if __name__ == "__main__":
    main()
