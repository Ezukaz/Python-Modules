#!/usr/bin/env python3
import sys
import os
import site


if __name__ == "__main__":
    has_env = False if sys.prefix == sys.base_prefix else True
    status = (
        "Welcome to the construct" if has_env else "You\'re still plugged in"
    )
    print(f"\nMATRIX STATUS: {status}")

    print(f"\nCurrent Python: {sys.executable}")
    env_path_msg = (
        f"{os.path.basename(sys.prefix)}\nEnvironment Path: {sys.prefix}"
    )
    env_msg = env_path_msg if has_env else "None detected"
    print(f"Virtual Environment: {env_msg}")

    if has_env:
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        try:
            print(f"{site.getsitepackages()[0]}")
        except (AttributeError, IndexError):
            print(site.getusersitepackages())
    else:
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")

        print("\nThen run this program again.")
