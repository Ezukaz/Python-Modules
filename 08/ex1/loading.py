#!/usr/bin/env python3
import importlib.metadata as meta
import importlib.util as util


def has_dependency(dep: str, msg: str) -> bool:
    if util.find_spec(dep):
        print(
            f"[OK] {dep.lower()} ({meta.version(dep)}) - "
            f"{msg.capitalize()} ready"
        )
        return True
    print(f"[MISSING] {dep.lower()} - No {msg.lower()}")
    return False


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    missing_dep = False
    print("\nChecking dependencies:")
    if not has_dependency("pandas", "data manipulation"):
        missing_dep = True
    if not has_dependency("matplotlib", "visualization"):
        missing_dep = True
    if not has_dependency("numpy", "numerical computation"):
        missing_dep = True

    if missing_dep:
        print("\nTo install dependencies: ", end="")
        print("pip install -r requirements.txt")
        print("                         poetry install (if using Poetry)")
    else:
        import numpy as np
        import pandas as pd
        import matplotlib as mp
        print("\nAnalyzing Matrix data...")
        data = np.random.randn(1000)
        print("Processing 1000 data points...")
        df = pd.DataFrame(data, columns=["value"])
        print(f"  Mean: {df['value'].mean():.2f}")
        print(f"  Max:  {df['value'].max():.2f}")
        print(f"  Min:  {df['value'].min():.2f}")
        print("Generating visualization...")
        df.plot()

        print("\nAnalysis complete!")
        mp.pyplot.savefig("matrix_analysis.png")
        print("Results saved to: matrix_analysis.png")
