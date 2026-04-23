#!/usr/bin/env python3

import os
from dotenv import load_dotenv, dotenv_values


def get_status(is_ok: bool) -> str:
    return f"{'[OK]' if is_ok else '[WARN]'}"


def add_prefix(is_ok: bool, suffix1: str, suffix2: str) -> str:
    return f"{suffix1 if is_ok else suffix2}"


def print_status_msg(is_ok: bool, msg: str) -> None:
    print(f"{get_status(is_ok)} {msg.capitalize()}")


def security_check() -> None:
    # all() returns True if all elements are truthy
    checks_ok = all([DATABASE_URL, API_KEY, ZION_ENDPOINT])
    msg = f"{add_prefix(checks_ok, 'no', '')} hardcoded secrets detected"
    print_status_msg(checks_ok, msg)

    # os.path.exists() returns True if that path exists
    is_dot_env = os.path.exists(".env")
    msg = f".env file {add_prefix(is_dot_env, '', 'im')}properly configured"
    print_status_msg(is_dot_env, msg)

    # dotenv_values() returns a dict of your .env file
    env_file = dotenv_values(".env")
    # any() returns True if any are True
    overrides = any([os.getenv(k) != env_file[k] for k in env_file])
    msg = f"production overrides {add_prefix(overrides, '', 'un')}available"
    print_status_msg(overrides, msg)


if __name__ == "__main__":
    # loads the .env contents into the env if they don't exist
    # if the key exists it will not override it unless you override=True
    load_dotenv()

    # setting globals
    # getenv to get the global env
    MATRIX_MODE = os.getenv("MATRIX_MODE", "development")
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

    print("\nORACLE STATUS: Reloading the Matrix...")

    print("\nConfiguration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    print(f"Database: {DATABASE_URL}")
    print(f"API Access: {API_KEY}")
    print(f"Log Level: {LOG_LEVEL}")
    print(f"Zion Network: {ZION_ENDPOINT}")

    print("\nEnvironment security check:")
    security_check()

    print("\nThe Oracle sees all configurations.")
