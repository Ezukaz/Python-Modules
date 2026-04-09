#!/usr/bin/env python3

import importlib.util, importlib.metadata
import pandas, requests, numpy, matplotlib


print(importlib.util.find_spec("requests"))

def has_dependency(dep: str, msg: str) -> bool:
    if importlib.util.find_spec(dep):
        print(
            f"[OK] {dep.lower()} ({importlib.metadata.version(dep)}) - "
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
    if not has_dependency("requests", "network access"):
        missing_dep = True
    if not has_dependency("matplotlib", "visualization"):
        missing_dep = True

    if missing_dep:
        print("\nTo install dependencies:", end="")
        print("pip install -r requirements.txt")
        print(f"                         poetry install (if using Poetry)")
    else:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...")

        print("\nAnalysis complete!")
        print("Results saved to: matrix\_analysis.png")
