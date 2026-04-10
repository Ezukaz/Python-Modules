#!/usr/bin/env python3

import sys


def process_commands(args: list[str]) -> None:
    """ Process and display command line arguments """
    print("=== Command Quest ===")

    program_name = args[0]
    print(f"Program name: {program_name}")
    total_args = len(args)
    if total_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")
        args = sys.argv[1:]
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {total_args}")
    print()


if __name__ == "__main__":
    process_commands(sys.argv)
