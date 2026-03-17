#!/usr/bin/env python3
"""Exercise 5: Stream Wizard - Generator-based data streaming"""

from typing import Generator
import time


def game_event_stream(count: int) -> Generator[str, None, None]:
    """Generate game events on-demand using yield."""
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]

    for i in range(count):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = levels[i % len(levels)]
        yield f"Event {i+1}: Player {player} (level {level}) {event}"


def fibonacci_stream(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci numbers on-demand."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_stream(n: int) -> Generator[int, None, None]:
    """Generate first n primes on-demand."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def demonstrate_streaming() -> None:
    """Demonstrate generator streaming capabilities."""
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()

    start_time = time.time()
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for i, event in enumerate(game_event_stream(1000)):
        if i < 3:  # Show first few
            print(event)
        if "level 12" in event:
            high_level_count += 1
        if "treasure" in event:
            treasure_count += 1
        if "leveled up" in event:
            levelup_count += 1

    end_time = time.time()

    print("...")
    print("\n=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    fibs = list(fibonacci_stream(10))
    print(", ".join(map(str, fibs)))

    print("Prime numbers (first 5):", end=" ")
    primes = list(prime_stream(5))
    print(", ".join(map(str, primes)))


if __name__ == "__main__":
    demonstrate_streaming()
